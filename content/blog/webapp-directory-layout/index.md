---
date: "2025-05-22T20:37:23+09:00"
title: "Webapp Directory Layout"
---

When building web applications, choosing the right directory structure is crucial for maintaining clean, scalable, and
efficient code. Each web framework has its own conventions and best practices for organizing code into folders and
files. Whether you're working with JavaScript, Go, Python, Java, Ruby, or PHP, following these conventions will help
ensure your project is maintainable and easily understood by other developers.

In this article, we explore the recommended directory structures for some of the most popular web frameworks in the
industry. You'll find folder-by-folder breakdowns along with official documentation links to help you dive deeper.
Whether you're starting a new project or restructuring an existing one, this article is a handy reference to keep your
projects organized and professional.

## Node.js Frameworks

### Express

Express is a minimal and flexible Node.js web application framework that provides a robust set of features for web and
mobile applications.

🌐 **Official Website**: [expressjs.com](https://expressjs.com/)

> There is no definitive answer to this question. The answer depends on the scale of your application and the team that
> is involved. To be as flexible as possible, Express makes no assumptions in terms of structure.
> -- [Express FAQ](https://expressjs.com/en/starter/faq.html)

I asked ChatGPT (4o) and Google Gemini (2.0 Flash) to make **Recommended Structure**, anyhow. Here is a file tree with
some markup for writing on a blog post. You can click the folder icons to expand or collapse the contents.

📁 Recommended Structure:

{{< filetree/container >}}
{{< filetree/folder name="project-root" >}}
{{< filetree/folder name="src" >}}
{{< filetree/file name="app.js" >}}
{{< filetree/folder name="config" >}}
{{< filetree/file name="index.js" >}}
{{< filetree/file name="development.js" >}}
{{< filetree/file name="production.js" >}}
{{< /filetree/folder >}}
{{< filetree/folder name="controllers" state="closed" >}}
{{< filetree/file name="user.controller.js" >}}
{{< filetree/file name="product.controller.js" >}}
{{< /filetree/folder >}}
{{< filetree/folder name="middlewares" state="closed" >}}
{{< filetree/file name="auth.middleware.js" >}}
{{< filetree/file name="error.middleware.js" >}}
{{< /filetree/folder >}}
{{< filetree/folder name="models" state="closed" >}}
{{< filetree/file name="user.model.js" >}}
{{< filetree/file name="product.model.js" >}}
{{< /filetree/folder >}}
{{< filetree/folder name="routes" state="closed" >}}
{{< filetree/file name="index.js" >}}
{{< filetree/file name="user.routes.js" >}}
{{< filetree/file name="product.routes.js" >}}
{{< /filetree/folder >}}
{{< filetree/folder name="services" state="closed" >}}
{{< filetree/file name="user.service.js" >}}
{{< filetree/file name="product.service.js" >}}
{{< /filetree/folder >}}
{{< filetree/folder name="utils" state="closed" >}}
{{< filetree/file name="logger.js" >}}
{{< filetree/file name="helper.js" >}}
{{< /filetree/folder >}}
{{< filetree/folder name="validations" state="closed" >}}
{{< filetree/file name="user.validation.js" >}}
{{< filetree/file name="product.validation.js" >}}
{{< /filetree/folder >}}
{{< filetree/folder name="views" state="closed" >}}
{{< filetree/folder name="layouts" state="closed" >}}
{{< filetree/file name="main.ejs" >}}
{{< /filetree/folder >}}
{{< filetree/folder name="partials" state="closed" >}}
{{< filetree/file name="header.ejs" >}}
{{< /filetree/folder >}}
{{< filetree/file name="index.ejs" >}}
{{< /filetree/folder >}}
{{< filetree/folder name="public" state="closed" >}}
{{< filetree/folder name="css" state="closed" >}}
{{< filetree/file name="style.css" >}}
{{< /filetree/folder >}}
{{< filetree/folder name="js" state="closed" >}}
{{< filetree/file name="script.js" >}}
{{< /filetree/folder >}}
{{< filetree/folder name="images" state="closed" >}}
{{< filetree/file name="logo.png" >}}
{{< /filetree/folder >}}
{{< /filetree/folder >}}
{{< /filetree/folder >}}
{{< filetree/folder name="tests" state="closed" >}}{{< /filetree/folder >}}
{{< filetree/folder name="node_modules" state="closed" >}}{{< /filetree/folder >}}
{{< filetree/file name="package.json" >}}
{{< filetree/file name=".env" >}}
{{< /filetree/folder >}}
{{< /filetree/container >}}

Key Components:

- `src/`: Contains all application source code.
  - `app.js`: The entry point of the application, initializes and starts the server.
  - `config/`: Stores configuration files for different environments.
  - `controllers/`: Handles request logic and interacts with services.
  - `middlewares/`: Functions that execute before or after route handlers.
  - `models/`: Defines data structures and interacts with the database.
  - `routes/`: Defines API endpoints and their corresponding handlers.
  - `services/`: Encapsulates business logic and data processing.
  - `utils/`: Provides reusable utility functions.
  - `validations/`: Contains schemas for validating request data.
  - `views/`: Contains template files used to render dynamic HTML content.
  - `public/`: Static assets (e.g., images, CSS, JavaScript).
- `tests/`: Holds test files for different parts of the application.

### Next.js

Next.js is a React framework for production that enables hybrid static & server rendering, TypeScript support, smart
bundling, route pre-fetching, and more.

🌐 **Official Website**: [nextjs.org](https://nextjs.org/)

> This page provides an overview of all the folder and file conventions in Next.js, and recommendations for organizing
> your project.
> -- [Next.js Project Structure and Organization](https://nextjs.org/docs/pages/getting-started/project-structure)

📁 **Top-level folders**:

- `app/`: App Router
- `pages/`: Pages Router
- `public/`: Static assets to be served
- `pages/`: Optional application source folder

The Project Structure page also provides an overview of folder and file conventions, including top-level files, routing,
and dynamic route patterns.

### Fastify

Fastify is a fast and low-overhead web framework for Node.js.

🌐 **Official Website**: [fastify.io](https://fastify.io/)

Fastify provides [fastify/demo](https://github.com/fastify/demo) on GitHub for a concrete example of a Fastify
application using what are considered best practices by the Fastify community.

📁 **Recommended Structure**:

- `app/`:
  - `plugins/`: Custom plugins.
  - `routes/`: Route definitions.
  - `schemas/`: JSON schemas for validation.
  - `app.ts`: Application entry point.
  - `server.ts`: An example for running an application as a standalone executable.
- `test/`:
  - `app/`
  - `plugins/`
  - `routes/`
- `scripts/`: Database models.
- `migrations/`: SQL files

## Go Frameworks

If your use case can be covered by Go’s standard library, it’s a good idea to use the net/http package. Some developers
have also published comparisons of different routing features.

[Which Go router should I use? – Alex Edwards](https://www.alexedwards.net/blog/which-go-router-should-i-use)

In this article, I checked four web frameworks.

### Gin

Gin is a HTTP web framework written in Go (Golang) featuring a Martini-like API with performance up to 40 times faster.

🌐 **Official Website**: [gin-gonic.com](https://gin-gonic.com/)

The Gin framework does not impose a strict official project folder structure. However, I asked ChatGPT (4o) to make
Recommended Structure which help developers organize their projects effectively.

📁 Recommended Gin Project Structure

```
your_project/
├── main.go               # Application entry point
├── go.mod                # Module definition
├── config/               # App configuration (e.g., env, settings)
├── routes/               # Route definitions
├── handlers/             # HTTP request handlers
├── models/               # Structs representing data models
├── repositories/         # Data access layer
├── services/             # Business logic layer
├── middlewares/          # Custom Gin middleware
├── utils/                # Utility functions/helpers
├── templates/            # HTML templates (if used)
├── public/               # Static files (e.g., images, JS, CSS)
├── test/                 # Unit & integration tests
└── docs/                 # Documentation (e.g., Swagger)
```

🧠 Philosophy

- Organized by functionality and responsibility.
- Separation of concerns: routing, business logic, and data access layers.
- Scales well for larger applications.

📌 Tip

You can simplify the structure for small projects by collapsing folders (e.g., combine controllers and routes), but this
layout is ideal as your application grows.

It could be helpful to see official examples and quick start guides.

- [gin-gonic/examples: A repository to host examples and tutorials for Gin.](https://github.com/gin-gonic/examples)
- [gin/docs/doc.md at master in gin-gonic/gin on GitHub](https://github.com/gin-gonic/gin/blob/master/docs/doc.md)

### Echo

Echo is a high performance, extensible, minimalist Go web framework.

🌐 **Official Website**: [echo.labstack.com](https://echo.labstack.com/)

While Echo does not impose a strict folder structure, Recommended Gin Project Structure above could be helpful.

### Chi

Chi is a lightweight, idiomatic and composable router for building Go HTTP services.

🌐 **Official Website**: [go-chi.io](https://go-chi.io/)

While Chi does not impose a specific project structure, Recommended Gin Project Structure above could be helpful.

### Hertz

Hertz is a high-performance, extensible, and minimalist Go web framework.

🌐 **Official Website**: [cloudwego.io](https://www.cloudwego.io/docs/hertz/)

Hertz supports IDL-based development because it's part of the CloudWeGo ecosystem, which emphasizes high-performance
microservices and service interoperability. The two most commonly used IDLs with Hertz are Thrift and Protocol Buffers.

In Hertz, IDL stands for Interface Definition Language. It's used to define the API's interface -- including service
methods, request and response types, and data structures -- in a way that is language-agnostic and machine-readable.

Why Use IDL with Hertz?

- 🚀 Auto-generates handler templates, routes, and models
- 🧩 Ensures consistency across services and clients
- 🔒 Strong typing and input validation from the start
- 🔄 Makes integration across services and languages easier

[hz layout](https://www.cloudwego.io/docs/hertz/tutorials/toolkit/layout/) shows the structure of the generated code.

📁 **Recommended Structure**:

- `biz/`: Business logic.
  - `handler/`
  - `model/`
  - `router/`
- `idl/`: defined IDL, location can be arbitrary
- `router.go`: User defined routing methods in addition to IDL
- `main.go`: Application entry point.

## Python Frameworks

### Django

Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.

🌐 **Official Website**: [djangoproject.com](https://www.djangoproject.com/)

Django encourages a project structure based on the principle of modularity and reusability. It recommends organizing
your code into multiple self-contained apps that each serve a specific purpose. This design pattern, often called "app
per domain" or "functional separation," helps keep large codebases maintainable and scalable.

When you create a Django project using `django-admin startproject`, you get the basic scaffold:

📁 Recommended Django Project Structure

```
your_project/
├── manage.py                    # Project management script
├── mysite/                      # Main site settings and URLs
│   ├── __init__.py
│   ├── settings.py              # Global configuration
│   ├── urls.py                  # Root URL configuration
│   ├── asgi.py
│   └── wsgi.py
├── apps/                        # Recommended: store all custom apps here
│   ├── users/                   # Example app (authentication, profiles)
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── forms.py
│   ├── blog/                    # Another example app
│   │   ├── ...
├── templates/                   # Shared HTML templates
├── static/                      # Global static files (CSS, JS, images)
├── media/                       # User-uploaded content
├── requirements.txt             # Dependency list
└── .env                         # Environment variables (optional)
```

🧠 Design Philosophy

- Each app should be independent and reusable.
- Apps communicate via import or Django signals.
- Business logic is organized into views, models, and optionally services or use-cases.
- Use Django’s configuration settings for environment-specific behavior.

✅ Best Practices

- Group reusable apps under apps/
- Use settings modules for environment separation (e.g., settings/dev.py, settings/prod.py)
- Use class-based views for reusability and clarity
- Keep apps small and focused on a single responsibility
- Leverage Django’s built-in features: Admin, ORM, middleware

🔗 Official References

- Tutorial: [Writing your first Django app, part 1](https://docs.djangoproject.com/en/stable/intro/tutorial01/)
- The development process: [Applications](https://docs.djangoproject.com/en/stable/ref/applications/)

### Flask

Flask is a lightweight WSGI web application framework in Python.

🌐 **Official Website**: [flask.palletsprojects.com](https://flask.palletsprojects.com/)

Flask is a micro web framework that gives you the flexibility to organize your project however you like. While simple
scripts can live in a single file, for anything beyond a small app, the Flask community recommends using a modular,
scalable layout.

Below is the recommended project structure for a Flask application that follows best practices for maintainability,
scalability, and testability.

📁 Recommended Flask Project Structure

```
your_project/
├── app/                         # Application package
│   ├── __init__.py              # App factory and initialization
│   ├── routes/                  # Route handlers (views/controllers)
│   │   └── user_routes.py
│   ├── models/                  # SQLAlchemy models
│   │   └── user.py
│   ├── services/                # Business logic
│   │   └── user_service.py
│   ├── templates/               # Jinja2 HTML templates
│   ├── static/                  # Static assets (CSS, JS, images)
│   ├── extensions.py            # App extensions (db, login_manager, etc.)
│   ├── config.py                # App configuration classes
│   └── utils/                   # Utility functions and helpers
│       └── helpers.py
├── migrations/                  # Database migrations (via Flask-Migrate)
├── tests/                       # Unit and integration tests
│   └── test_user.py
├── .env                         # Environment variables
├── requirements.txt             # Python dependencies
├── run.py                       # Entry point to start the app
└── README.md
```

🧠 Key Concepts

- App Factory Pattern: Define a **create_app()** function in `app/__init__.py` to create and configure the Flask
  application dynamically.
- Blueprints: Organize views into reusable components using Flask blueprints (e.g., one per feature or module).
- Extensions: Initialize Flask extensions (SQLAlchemy, Migrate, LoginManager, etc.) in extensions.py and import them in
  your app.

✅ Best Practices

- Use environment-based configuration (development, testing, production).
- Separate business logic (services) from request-handling (routes).
- Modularize by feature/domain (especially with blueprints).
- Use Flask CLI for development tasks.
- Integrate pytest or unittest for testing.

🔗 Official Resources + Blog series

- [Application Factories](https://flask.palletsprojects.com/en/latest/patterns/appfactories/)
- [Modular Applications with Blueprints](https://flask.palletsprojects.com/en/latest/blueprints/)
- [The Flask Mega-Tutorial, Part I: Hello, World!](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
  in a series of 23 chapters on blog.miguelgrinberg.com

### FastAPI

Fast API is a modern, fast (high-performance) web framework for building APIs based on standard Python type hints.

🌐 **Official Website**: [fastapi.tiangolo.com](https://fastapi.tiangolo.com/)

FastAPI encourages a modular, clean, and scalable project structure, especially for medium to large projects.

📁 Recommended FastAPI Project Structure

```
your_project/
├── app/                          # Application package
│   ├── main.py                   # FastAPI app instance and entry point
│   ├── api/                      # API routers (grouped by feature)
│   │   ├── __init__.py
│   │   ├── users.py
│   │   └── items.py
│   ├── core/                     # Core app settings/configuration
│   │   ├── config.py
│   │   └── security.py
│   ├── models/                   # Pydantic models and/or ORM models
│   │   ├── user.py
│   │   └── item.py
│   ├── crud/                     # CRUD operations (DB access layer)
│   │   ├── user.py
│   │   └── item.py
│   ├── db/                       # Database initialization and session management
│   │   ├── base.py
│   │   ├── session.py
│   │   └── base_class.py
│   ├── schemas/                  # Pydantic schemas for request/response validation
│   │   ├── user.py
│   │   └── item.py
│   ├── services/                 # Business logic layer (optional)
│   │   └── user_service.py
│   ├── utils/                    # Helper functions/utilities
│   │   └── helpers.py
│   ├── middlewares/              # Custom middleware
│   └── tests/                    # Test cases
│       ├── __init__.py
│       └── test_users.py
├── alembic/                      # DB migration scripts (if using Alembic)
├── requirements.txt              # Python dependencies
├── .env                          # Environment variables
└── README.md
```

🧠 Design Philosophy

- Separate API routes from business logic and data layers.
- Use Pydantic models for data validation and serialization.
- Keep database models, CRUD logic, and schemas distinct.
- Modularize by feature (e.g., users, items).
- Make use of dependency injection to keep code clean and testable.

✅ Best Practices

- Use an app factory pattern (optional, but useful for large projects).
- Use Alembic or another migration tool to manage database schema changes.
- Write tests under the `tests/` directory.
- Keep configuration in a dedicated module.
- Organize routes using FastAPI routers for better modularity.

🔗 Official Resources

- [Bigger Applications - Multiple Files](https://fastapi.tiangolo.com/tutorial/bigger-applications/)
- [Dependency Injection](https://fastapi.tiangolo.com/tutorial/dependencies/)
- [Testing](https://fastapi.tiangolo.com/tutorial/testing/)
- [Full Stack FastAPI Template](https://fastapi.tiangolo.com/project-generation/)

## Java Framework

### Spring Boot

Spring Boot is a framework that simplifies the development of new Spring applications.

🌐 **Official Website**: [spring.io](https://spring.io/projects/spring-boot)

Spring Boot follows a convention-over-configuration philosophy and encourages a clean, layered architecture. The
official recommendation is to organize your project by feature or by technical layer using standard Maven/Gradle layout.

Here's a recommended structure that promotes modularity, scalability, and clarity in Spring Boot projects:

📁 Recommended Spring Boot Project Structure

- `src/main/java/{myapplication}/`: Application source code.
- `src/main/resources/`: Configuration files and templates.
  - `application.properties`: App config
  - `static/`: Static assets
  - `templates/`: Thymeleaf templates (if using)
- `src/test/java/`: Test cases.
- `pom.xml` or `build.gradle`: Dependencies and build setup
- `README.md`

Example Java classes.

```
src/main/java/com/example/myapp/
├── MyAppApplication.java       # Main app class with @SpringBootApplication
├── customer/                   # A domain feature (sub-package)
│   ├── Customer.java           # Domain model
│   ├── CustomerRepository.java # Repository
│   ├── CustomerService.java    # Service
│   └── CustomerController.java # Web controller
└── shared/                     # Optional: shared utilities/config
    ├── config/
    │   └── AppConfig.java
    └── exception/
        └── GlobalExceptionHandler.java
```

📌 Key Points from the Spring Docs:

- Keep the main class in the root package (e.g., `com.example.myapp`).
- Group features by sub-package (e.g., customer, order, billing).
- Spring automatically scans sub-packages, making component discovery seamless.
- This structure avoids having to manually specify `@ComponentScan`.

🔗 Official Resources

- [Structuring Your Code](https://docs.spring.io/spring-boot/docs/current/reference/html/using.html)

## Ruby Framework

### Ruby on Rails

Ruby on Rails is a web-application framework that includes everything needed to create database-backed web applications
according to the Model-View-Controller (MVC) pattern.

🌐 Official Website: [rubyonrails.org](https://rubyonrails.org/)

Ruby on Rails is a full-stack web framework that follows “Convention over Configuration” and “Don’t Repeat Yourself”
philosophies. Rails projects have a very standardized, opinionated directory layout designed to streamline development
and encourage best practices.

📁 Recommended Ruby on Rails Project Structure

```
your_rails_app/
├── app/                       # MVC architecture and core application code
│   ├── assets/                # CSS, JavaScript, images, fonts
│   ├── controllers/           # Controllers handle web requests
│   ├── helpers/               # View helpers
│   ├── models/                # ActiveRecord models
│   ├── views/                 # View templates (ERB, Haml, etc.)
│   ├── channels/              # ActionCable WebSocket channels
│   └── jobs/                  # Background jobs (ActiveJob)
├── bin/                       # Executable scripts (rails, rake, etc.)
├── config/                    # Application configuration
│   ├── environments/          # Environment-specific settings (development, test, production)
│   ├── initializers/          # Bootstrapping code and third-party gem configs
│   ├── locales/               # i18n translation files
│   ├── routes.rb              # Route definitions
│   └── application.rb         # Main app config
├── db/                        # Database schema, migrations, seeds
├── lib/                       # Custom libraries and extensions
│   ├── tasks/                 # Custom rake tasks
├── log/                       # Log files
├── public/                    # Static files served directly by the web server
├── test/ or spec/             # Tests (depending on testing framework, e.g., Minitest or RSpec)
├── tmp/                       # Temporary files (cache, pid, sessions)
├── vendor/                    # Third-party code and plugins
├── Gemfile                    # Project dependencies
├── Rakefile                   # Task runner
└── README.md
```

🧠 Design Philosophy

- Follows the MVC pattern: Models, Views, Controllers.
- Convention-driven file and directory layout.
- Emphasizes “fat models, skinny controllers” — business logic lives mostly in models.
- Built-in generators to scaffold models, controllers, tests, etc.
- Supports RESTful routing by default.

✅ Best Practices

- Organize code in `app/` by function (models, controllers, views).
- Use `lib/` for shared code that doesn’t fit MVC.
- Keep environment-specific configs under `config/environments/`.
- Use migrations to evolve database schema (`db/migrate/`).
- Write tests in `test/` or `spec/` (RSpec).
- Use assets pipeline in `app/assets/` for CSS/JS/images.

🔗 Official Resources

- [Getting Started with Rails](https://guides.rubyonrails.org/getting_started.html#directory-structure) - 3.3. Directory
  Structure
- [The Rails Command Line](https://guides.rubyonrails.org/command_line.html) - `rails new`

## PHP Framework

### Laravel

Laravel is a web application framework with expressive, elegant syntax.

🌐 Official Website: [laravel.com](https://laravel.com/)

Laravel is a PHP web framework known for its elegant syntax, built-in tools, and emphasis on developer productivity. It
follows the MVC (Model–View–Controller) pattern and provides a clear, structured project layout out-of-the-box. Its
default directory structure is already well-suited for most applications and considered a best practice by the Laravel
community.

📁 Recommended Laravel Project Structure (Default Best Practice)

```
your-laravel-app/
├── app/                      # Core application code (MVC)
│   ├── Console/              # Artisan commands
│   ├── Exceptions/           # Custom exception handling
│   ├── Http/
│   │   ├── Controllers/      # Controllers for handling routes
│   │   ├── Middleware/       # HTTP middleware
│   │   └── Kernel.php        # HTTP kernel
│   ├── Models/               # Eloquent models (Laravel 8+)
│   ├── Policies/             # Authorization logic
│   ├── Providers/            # Service providers (app bootstrapping)
│   └── Services/             # (Optional) Business logic services
├── bootstrap/                # App bootstrapping, including app.php
│   └── cache/                # Cached files (routes, config, services)
├── config/                   # Configuration files (app, db, mail, etc.)
├── database/
│   ├── factories/            # Model factories for testing/seeding
│   ├── migrations/           # Database migrations
│   └── seeders/              # Data seeders
├── public/                   # Web root, contains index.php
├── resources/
│   ├── js/                   # JavaScript files (Vue, React)
│   ├── css/                  # Stylesheets
│   ├── lang/                 # Localization files
│   └── views/                # Blade view templates
├── routes/
│   ├── web.php               # Web routes
│   ├── api.php               # API routes
│   └── console.php           # Console command routes
├── storage/                  # Logs, compiled views, file uploads
│   ├── app/
│   ├── framework/
│   └── logs/
├── tests/                    # Unit and feature tests (PHPUnit)
│   ├── Feature/
│   └── Unit/
├── vendor/                   # Composer dependencies
├── .env                      # Environment config
├── composer.json             # PHP dependencies
└── artisan                   # Laravel CLI entry point
```

🧠 Laravel Philosophy

- “Convention over Configuration” but with flexibility.
- Clean separation of concerns: Controllers, Models, Views, Middleware, Services.
- Encourages RESTful routing and resource controllers.
- Provides first-class testing, migration, validation, and auth scaffolding.

✅ Best Practices

- Use Services or Actions folders (app/Services or app/Actions) for business logic.
- Organize tests under tests/Feature and tests/Unit.
- Use route model binding for cleaner controllers.
- Follow the Single Responsibility Principle (SRP) — thin controllers, fat models/services.
- Use environment configuration for flexibility (.env files).
- Use Laravel’s dependency injection and service container to manage class dependencies.

🔗 Official Resources

- [Laravel Directory Structure](https://laravel.com/docs/structure)

## Summary

In summary, understanding and following the recommended directory structures of web frameworks is essential for building
scalable, maintainable, and efficient applications. Whether you're working with frontend frameworks like Next.js,
backend powerhouses like Spring Boot and Django, or microframeworks such as Flask and Express, each framework promotes a
structure that reflects its core philosophy and development workflow. Adhering to these conventions not only helps you
onboard faster but also aligns your codebase with community standards—making collaboration, testing, and deployment much
smoother. As your project grows, a well-organized structure becomes a powerful ally in managing complexity and promoting
clean, modular code.
