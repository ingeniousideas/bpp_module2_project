# bpp_module2_project

Repository for the bpp apprenticeship module 2 assessment.

## Applicaiton Development

### Prototype Apps

- dash_app/app_20.py
- dash_app/app_minimal.py
  - Retrives csv data from online Plotly repository.
  - Single page with **Dropdown** and reactive **Line Graph**.

- doraview/app.py
  - Retrives csv data from online Plotly repository.
  - Added dataframes that read frm **JSON files**.
    - These are the **mock data**.
  - Displays Plotly data in **Table** and **Bar Chart**.
  - Displays **JSON** data only as **Tables**.

## DevOps Research Assessment (DORA)

This is composed of four key metrics, that are divided into thorughput of software changes, and stability of software changes <https://dora.dev/guides/dora-metrics-four-keys/>.

### Throughput

Throughput measures the velocity of changes that are being made. DORA assesses throughput using the following metrics:

- **Change lead time:** This metric measures the time it takes for a code commit or change to be successfully deployed to production. It reflects the efficiency of your software delivery process.
- **Deployment frequency:** This metric measures how often application changes are deployed to production. Higher deployment frequency indicates a more efficient and responsive delivery process.

### Stability

Stability measures the quality of the changes delivered and the team’s ability to repair failures. DORA assesses stability using the following metrics:

- **Change fail percentage:** This metric measures the percentage of deployments that cause failures in production, requiring hotfixes or rollbacks. A lower change failure rate indicates a more reliable delivery process.
- **Failed deployment recovery time:** This metric measures the time it takes to recover from a failed deployment. A lower recovery time indicates a more resilient and responsive system.

## Report

A written report (maximum 2000 words +/- 10%) that describes the business need/problem you are aiming to solve, and how you intend to solve it using an application, including:

- Defend your choices for the architecture for your application including any hardware
considerations or requirements.
- Critically appraise what additional work is required to turn the prototype into a fully
working application, including any changes from feedback.
- Consider how your application could be utilised in a smart, IoT environment.
- Include code snippets from your application to demonstrate the concepts applied.

## Video Demo

This uses the Role Profiles, User Stories and Uses Cases as defined in [User Centric Desing](#user-centric-design) below.
Showcase in Video

Plan for 5-minute demo could show:

- Login/role selection (1 min)
- Dashboard view with four DORA metrics (2 min)
- Filtering and drilling into a specific metric (1.5 min)
- Export or summary screen (0.5 min)

This flow mirrors how each user profile benefits from the system and links to your design and business justification in the report.

## TODO

- Refer to Topic 6 Experiment Jup Notebook.
  - Use of Async and Redis as a data cache.
  - Implement it and say in report how it could be used for production.
    - Code snippet.
  - massive numbers of servers and deployments etc.
  - To deliver perfomance optimisation strategies that ensure scalable system performance.

- Be sure to include the diagrams.
  - Class Diagram for anything OOP.
  - Activity for concurrnent processes.
  - Etc.

- Design Patterns should also be referenced and referred to where applicable.
  - May not actually use one.
  - Mor than likely though.

- Be sure to add an architectral diagram of the whole system.
  - Doesn't need to be in UML, as might not be suitable.
  - Higher level abstraction that should visually show the structure and flow of the system.
  - N.B. Focus is on the front-end usability.
    - Backend likely just to be stubbed out.
    - No need for backend really.
    - All this can be just dicussed in future works.

## User Centric Design

The design should be centred on the User Experience and their particular needs with respects to their role and responsiblites.

### 1. Define User Profiles

Who are the users of this application, and what are they likely to want to know. What would be their scope of interest, and level of detail? This will inform what visualisations and functionality need to be written into the application.

| **User Profile**            | **Role in Organisation**               | **Motivations for Using the App**                                                                               | **Typical Actions**                                                  |
| --------------------------- | -------------------------------------- | --------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **Lab Engineering Lead**    | Oversees multiple delivery teams       | Needs to track deployment frequency, lead time, and reliability to report productivity and identify bottlenecks | View overall DORA dashboards, filter by team/project, export reports |
| **DevOps Engineer**         | Manages CI/CD pipelines                | Monitors stability, deployment success/failure rates, and recovery times                                        | View deployment logs, identify trends, drill down into incidents     |
| **Software Engineer**       | Builds and deploys code                | Wants feedback on performance metrics of deployments to improve delivery speed                                  | View own team’s metrics, compare release cycle times                 |
| **Product Owner**           | Defines backlog and release priorities | Seeks insight into delivery velocity and system reliability to plan releases                                    | View release cadence and lead times for features                     |
| **Senior Management / CTO** | Strategic decision-making              | Needs aggregated view of software delivery performance to inform resourcing and investment                      | View summary dashboard, trend over time, KPI targets                 |

### 2. Derive User Stories

To describe an atomic behaviour and outcome that would be executed by a particular user.

Include the typical components:

- As a [User. Insert role.],
- I want [Goal. Insert what information wanted or actions performed etc.]
- So that [Benefit. Insert reason behind action or infromation request. Provides context for design.]
- Accpetence Criteria
  - What would fulfill the Use Case.

#### ChatGPT User Story Examples

- As an Engineering Manager, I want to view deployment frequency trends per application so that I can identify delivery bottlenecks.
- As a DevOps Engineer, I want to drill into failed deployments so that I can find root causes quickly.
- As a Product Owner, I want to see lead time for changes so that I can predict release readiness.

Each story naturally maps to a use case, UI component, and mocked backend function.

### 3. Infer Use Cases

These can be described in UML to highlight the interactin components of the system. This will then help to identify the various OOP Classes and mocked data that need to be defined and built.

#### ChatGPT Use Case Examples

Use cases describe how the system fulfils those user stories. For your prototype, you could select 3–4 concise, demonstrable ones:

1. View DORA Overview Dashboard – User logs in, selects application, and sees all four metrics visualised.
2. Filter Metrics by Application or Date Range – User narrows view to one application or sprint period.
3. Drill into a Metric (e.g., Deployment Frequency) – User clicks a chart segment to see deployment logs.
4. Export or Share Report – User exports metrics summary for review meeting.

These use cases are perfect for a five-minute video demo: short, visual, and directly linked to business value.

#### 4. Translate to Applicaiton Design

From these use cases, you can derive both UI elements and supporting logic:

- **UI Components:** dashboard charts (e.g. bar/line for trends, donut for proportions), filters, navigation bar, modal for metric details, export button.
- **Logic / Mocked Code:**
  - Mock datasets for each metric (JSON or SQLite tables),
  - Simple functions to filter by app/date,
  - Simulated API layer to fetch metric data,

Basic authentication simulation (for role-based access).

## jupyter_protoyping folder

This folder is for the prototyping of code with jupyter notebook.

Will have a separate venv to the main project to keep dependencies clean.

## Use of efficient algorithms

- Using approproate data structures.
- Optimising database queries.
- Implementing caching strategies.

### Parallel processing

This involves distributing workload across multiple processors or nodes to achieve faster execution. Techniques like multi-threading, message passing, and distributed computing frameworks (e.g., Apache Spark) enable parallel processing. Parallel processing improves scalability by leveraging the computing power of multiple resources and reducing the overall processing time.
