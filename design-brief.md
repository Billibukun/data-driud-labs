# Design Brief: Druid Labs Learning Platform Interface

## 1. Project Overview

This document outlines the design requirements for the web interface of the Druid Labs Learning Platform. The backend content, consisting of Jupyter notebooks and Markdown files, has been created and organized into a clear directory structure. The goal of the front-end is to present this content to students (age 12+) in an engaging, intuitive, and educational manner.

## 2. Target Audience

-   **Primary:** Secondary school students, age 12-18.
-   **Key Characteristics:** Varying levels of technical skill, from absolute beginners to potentially advanced learners. The design should be friendly, encouraging, and not intimidating.

## 3. Core User Experience Goals

-   **Clear Progression:** Students should always understand where they are in the curriculum, what they've completed, and what's next.
-   **Interactive Learning:** The interface should seamlessly integrate the JupyterLite environment to allow students to run code directly on the page.
-   **Sense of Accomplishment:** The design should incorporate visual cues (e.g., progress bars, checkmarks) to give students a sense of achievement as they complete modules.

## 4. Key Pages & Features

### 4.1. Dashboard / Home Page

-   This should be the main landing page for a logged-in student.
-   It should display all available courses (Python, SQL, JavaScript).
-   Each course should have a progress indicator (e.g., "3/9 Modules Completed").
-   Should provide a clear "Continue Learning" button that takes the student to their last viewed lesson.

### 4.2. Course Page

-   This page displays the curriculum for a single course (e.g., Python).
-   The content should be organized into the modules as defined in the `contents/` directory structure.
-   Each module should be expandable/collapsible to show the lessons within it.
-   Completed lessons and modules should be clearly marked (e.g., with a checkmark).

### 4.3. Lesson Page

-   This is the core of the learning experience.
-   It should render the content of a single `.ipynb` or `.md` file.
-   **For `.ipynb` files:**
    -   The page must embed a running JupyterLite kernel.
    -   Markdown cells should be rendered as formatted text.
    -   Code cells should be executable, with a clear "Run" button.
    -   Output from code cells should be displayed directly below the cell.
-   **For `.md` files:**
    -   The page should render the Markdown content as clean, readable, formatted text.
-   **Navigation:**
    -   A persistent sidebar or header should show the full course curriculum, with the current lesson highlighted.
    -   Clear "Previous Lesson" and "Next Lesson" buttons should be present.
    -   A "Mark as Complete" button should be available. When clicked, this should update the user's progress and automatically navigate to the next lesson.

## 5. Content Structure Reference

The content is organized in the `contents/` directory as follows:

```
contents/
├── data/                  # Sample data files for lessons
├── javascript/            # JavaScript Course
│   ├── 01-Introduction-to-JavaScript.ipynb
│   └── ...
├── python/                # Python Course
│   ├── 01-Python-Fundamentals/
│   │   ├── 01-Introduction-to-Python-and-Jupyter.ipynb
│   │   └── ...
│   ├── 02-Intermediate-Python/
│   └── ...
└── sql/                   # SQL Course
    ├── 01-Introduction-to-Databases-and-SQL.ipynb
    └── ...
```

The front-end should dynamically generate the course and lesson pages based on this structure.

## 6. Visual Design & Tone

-   **Clean & Modern:** Avoid clutter. Use plenty of white space.
-   **Engaging & Fun:** Use a friendly color palette. Consider subtle animations or illustrations to make the experience more enjoyable.
-   **Responsive:** The design must work flawlessly on desktops, tablets, and mobile devices.

This brief should provide a solid foundation for a front-end developer to begin designing and building the user interface for the Druid Labs platform.
