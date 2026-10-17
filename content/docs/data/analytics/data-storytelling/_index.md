---
date: "2026-10-17T09:00:00+09:00"
title: "Data Storytelling"
weight: 2
prev: "/docs/data/analytics/data-understanding"
next: "/docs/data/analytics"
---

Data storytelling is the practice of communicating an analytical finding through evidence, narrative, and visual representation. It helps an audience understand what the data shows, why the finding matters, and what decision or action may follow.

A chart or report can answer a narrow question without making its implications clear. A data story adds the context and reasoning that let people interpret the evidence. It is especially useful when an analysis concerns a specific decision, event, or change. A dashboard remains better suited to recurring monitoring and exploration; a story is usually a deliberate, focused communication.

## Three Elements of a Data Story

Effective data storytelling brings together three elements. None can compensate for a weakness in the others.

| Element       | Role                                         | Questions it should answer                                                      |
| ------------- | -------------------------------------------- | ------------------------------------------------------------------------------- |
| **Data**      | Provides the evidence and its limits         | What was measured? For whom and when? How reliable and complete is it?          |
| **Narrative** | Connects evidence to a point                 | What is the central message? What context and reasoning does the audience need? |
| **Visuals**   | Makes patterns and comparisons easier to see | Which visual form makes this evidence clear and accessible?                     |

The data includes more than headline figures: it includes definitions, methods, source context, and uncertainty. The narrative gives the evidence a logical order, often moving from a situation to a finding and its implication. Visuals may include charts, maps, tables, annotations, photographs, or interactive displays. Their purpose is to clarify the evidence and guide attention, not to decorate it.

These elements reinforce one another. A compelling narrative cannot rescue unreliable data; accurate data can still be misunderstood without context; and a polished visualization can mislead if its scales or encodings distort the comparison.

## A Practical Workflow

### 1. Start with the audience and decision

Identify who needs the information, what they already know, and what decision or question the communication should support. Define the relevant time horizon and available actions. A story for an executive deciding whether to fund an intervention will need different context and detail from a technical review of the underlying analysis.

### 2. Validate the evidence

Confirm the data's source, definitions, population, time period, and collection method. Check for missingness, inconsistent measurement, sampling bias, and changes in how the data was produced. Compare the results with an appropriate baseline. Data must be fit for the question, not merely available.

### 3. Find and test the insight

Explore the data to identify a meaningful pattern, difference, or change. Then test whether the apparent finding persists under reasonable alternative definitions, time windows, and segment comparisons. Look for competing explanations. A pattern is an observation; an explanation requires additional evidence.

### 4. Write the central message

Summarize the main finding in one sentence before designing slides or charts. A useful message is specific enough to be checked against the evidence and relevant to the audience's decision. If the sentence relies on a causal claim, confirm that the analysis supports causality; otherwise describe an association or observed change.

### 5. Build a logical narrative

Arrange the material so that readers can follow the reasoning. A simple structure is:

1. **Situation:** What question or condition makes this analysis relevant?
2. **Finding:** What did the evidence show?
3. **Explanation:** What factors may account for it, and how strong is that evidence?
4. **Implication:** Why does the finding matter to this audience?
5. **Action or open question:** What should happen next, or what remains uncertain?

Not every story needs a dramatic arc. Make the evidence easy to evaluate, and include relevant findings that qualify or challenge the central message.

### 6. Choose visuals for the question

Select a visual form that matches the comparison: a line chart for change over time, a bar chart for category comparisons, a scatterplot for relationships, or a map when location is itself meaningful. Use a table when readers need precise values. Label units and time periods, provide a descriptive title, and add annotations only when they help explain the evidence.

### 7. Review and refine

Check whether the story is understandable without an oral explanation, especially if it will be read asynchronously. Ask a colleague from the intended audience to summarize the main finding and its limits. Revise where readers misinterpret the chart, miss an assumption, or cannot identify the decision at stake.

## Principles for Credible Stories

### Lead with the finding and show its context

Use a clear headline that states the main finding rather than a generic label such as “Monthly results.” Include enough context to interpret it: the population, period, baseline, units, and relevant definitions. A change from 4% to 5% is one percentage point (a 25% relative increase); a change from 40% to 50% is ten percentage points (also a 25% relative increase).

### Separate observation, interpretation, and recommendation

Make the reasoning visible. For example:

- **Observation:** Support requests rose after a product release.
- **Interpretation:** The increase is concentrated in one affected workflow, which is consistent with a usability problem.
- **Recommendation:** Investigate that workflow and compare outcomes before and after a targeted change.

The first statement describes the data. The second offers an explanation that may need further testing. The third proposes an action. Keeping them distinct helps an audience judge the strength of each claim.

### Represent comparisons honestly

Use consistent scales when comparing charts, make the baseline clear, and avoid visual encodings that exaggerate differences. A truncated axis can be appropriate for some line charts when clearly shown, but it can make small changes look large; bars that encode magnitude should generally start at zero. Do not omit inconvenient periods, categories, or uncertainty simply to strengthen a preferred conclusion.

### Communicate uncertainty and limitations

State important assumptions, gaps, and sources of uncertainty in plain language. When estimates have meaningful uncertainty, show it with appropriate intervals or explain why a precise comparison is not supported. Do not claim that one factor caused another based only on correlation or sequence in time. A recommendation should reflect the strength of the evidence and the cost of being wrong.

### Match detail to the audience

Keep the main path focused, then provide supporting definitions, methods, or detailed results where readers can find them. A concise presentation need not hide complexity: it should make the key reasoning accessible while preserving a route to the evidence behind it.

## Worked Example: A Hypothetical Service Change

The following figures are invented to demonstrate the reasoning; they are not evidence about a real service.

Suppose a team observes that help requests increased after an interface change. In a hypothetical analysis, requests per 1,000 active users rise from 12 to 18 in the affected workflow, while comparable workflows remain near their earlier level. The team also finds that most additional requests concern the same step in the new interface.

| Stage         | Example                                                                                                                                                              |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Data**      | A hypothetical increase from 12 to 18 requests per 1,000 active users for one workflow; other workflows are a comparison, not proof of causation.                    |
| **Insight**   | The increase is concentrated in the workflow affected by the interface change and in questions about one step.                                                       |
| **Narrative** | “Requests rose in the changed workflow, and most additional requests concern the same step.” This describes the pattern without claiming that the release caused it. |
| **Visual**    | A line chart of requests per 1,000 users over time, marking the release date and showing the comparison workflow on the same scale.                                  |
| **Action**    | Review the step with users, test a targeted improvement, and measure whether the request rate changes.                                                               |

The story gives decision-makers a reason to investigate a focused part of the experience. It does not establish causation: seasonality, user mix, or other simultaneous changes could also explain the pattern. A controlled experiment or stronger comparison may be needed before attributing the change to the interface.

## Tools and Techniques

Choose tools according to the data, audience, delivery format, and maintenance needs. A spreadsheet may be sufficient for a small, one-off analysis. Statistical languages and visualization libraries can support repeatable analysis and custom charts. Business intelligence platforms are useful for governed recurring reports and interactive exploration. For location-centered stories, mapping tools may be appropriate; for a guided web narrative, a publishing or web-development workflow may be better.

Examples include Tableau or Power BI for business intelligence, Python or R visualization libraries for reproducible analysis, and QGIS for geographic analysis. These tools serve different purposes and change over time; assess accessibility, privacy, cost, collaboration, and export requirements before selecting one. Tool choice does not replace a clear question, sound analysis, or editorial review.

Data storytelling also overlaps with **digital storytelling**, a broader practice of using digital media—such as images, sound, video, and interactive elements—to share personal, educational, journalistic, or community stories. A data story may use these forms, but its defining evidence comes from data analysis. Digital storytelling does not necessarily depend on quantitative data.

## Further Reading

- Segel, E. and Heer, J. [“Narrative Visualization: Telling Stories with Data.”](https://doi.org/10.1109/TVCG.2010.179) _IEEE Transactions on Visualization and Computer Graphics_, 2010. A research study of narrative visualization techniques and design patterns.
- Nussbaumer Knaflic, C. [_Storytelling with Data: A Data Visualization Guide for Business Professionals._](https://www.oreilly.com/library/view/storytelling-with-data/9781119621492/) Wiley, 2015. A practical guide to communicating analytical results.
- UK Office for National Statistics. [“Showing uncertainty in charts.”](https://service-manual.ons.gov.uk/data-visualisation/guidance/showing-uncertainty-in-charts) Guidance on representing uncertainty in statistical charts.
- UK Office for National Statistics. [“Axes and gridlines.”](https://service-manual.ons.gov.uk/data-visualisation/guidance/axes-and-gridlines) Guidance on chart axes and comparable scales.
- StoryCenter. [“Our Story.”](https://www.storycenter.org/history) Background on the community practice of digital storytelling.

## Summary

Data storytelling connects validated evidence, a clear narrative, and purposeful visuals to help an audience interpret a finding and decide what to do. A credible story makes its reasoning and limitations visible. Use it when a focused communication can support understanding or action, and use recurring reports or dashboards when people need to monitor and explore changing data over time.
