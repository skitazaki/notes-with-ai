package main

import (
	"context"
	"fmt"
	"log"
	"net/http"
	"os"
	"os/signal"
	"syscall"
	"time"

	"github.com/go-redis/redis/v8"
	"github.com/jackc/pgx/v5"
	"github.com/kelseyhightower/envconfig"
	"github.com/prometheus/client_golang/prometheus/promhttp"
)

type App struct {
	DB    *pgx.Conn
	Redis *redis.Client
}

type Config struct {
	Port        string `envconfig:"PORT" default:"8080"`
	DatabaseURL string `envconfig:"DATABASE_URL" required:"true"`
	RedisURL    string `envconfig:"REDIS_URL" required:"true"`
}

func main() {
	// --- Load config from env (12-factor friendly)
	var cfg Config
	if err := envconfig.Process("", &cfg); err != nil {
		log.Fatalf("failed to load config: %v", err)
	}
	port := cfg.Port
	dbURL := cfg.DatabaseURL
	redisURL := cfg.RedisURL

	// --- Connect to PostgreSQL with pgx
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	db, err := pgx.Connect(ctx, dbURL)
	cancel()
	if err != nil {
		log.Fatalf("failed to connect to DB: %v", err)
	}
	defer db.Close(context.Background())

	// --- Connect to Redis
	opt, err := redis.ParseURL(redisURL)
	if err != nil {
		log.Fatalf("invalid Redis URL: %v", err)
	}
	rdb := redis.NewClient(opt)

	app := &App{DB: db, Redis: rdb}

	// --- Routes
	mux := http.NewServeMux()
	mux.HandleFunc("/healthz", app.handleHealthz)
	mux.HandleFunc("/readyz", app.handleReadyz)
	mux.Handle("/metrics", promhttp.Handler())

	mux.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintln(w, "Hello from Go webapp!")
	})

	srv := &http.Server{
		Addr:    ":" + port,
		Handler: mux,
	}

	// --- Start server
	go func() {
		log.Printf("Starting server on %s", srv.Addr)
		if err := srv.ListenAndServe(); err != nil && err != http.ErrServerClosed {
			log.Fatalf("listen error: %v", err)
		}
	}()

	// --- Graceful shutdown
	stop := make(chan os.Signal, 1)
	signal.Notify(stop, syscall.SIGTERM, syscall.SIGINT)

	<-stop
	log.Println("Shutting down gracefully...")

	ctx, cancel = context.WithTimeout(context.Background(), 8*time.Second)
	defer cancel()

	if err := srv.Shutdown(ctx); err != nil {
		log.Fatalf("Server Shutdown: %v", err)
	}

	log.Println("Goodbye!")
}

func (a *App) handleHealthz(w http.ResponseWriter, _ *http.Request) {
	// Simple: if server is running, it's alive
	w.WriteHeader(http.StatusOK)
	w.Write([]byte("ok"))
}

func (a *App) handleReadyz(w http.ResponseWriter, _ *http.Request) {
	ctx, cancel := context.WithTimeout(context.Background(), 2*time.Second)
	defer cancel()

	// Check DB
	if err := a.DB.Ping(ctx); err != nil {
		http.Error(w, "DB not ready", http.StatusServiceUnavailable)
		return
	}

	// Check Redis
	if _, err := a.Redis.Ping(ctx).Result(); err != nil {
		http.Error(w, "Redis not ready", http.StatusServiceUnavailable)
		return
	}

	w.WriteHeader(http.StatusOK)
	w.Write([]byte("ready"))
}
