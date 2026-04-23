#  Eitaa Scraper (Selenium)

> ⚠️ **[ARCHIVED] - Beginner Python Project (2023)**
> 
> *This repository contains one of my very first Python projects. It is kept public strictly for historical purposes to demonstrate my learning curve and growth as a developer. I do not maintain this code anymore.*

## About
This was a basic web scraping script built using **Python** and **Selenium** to extract view counts and data from channels on the Eitaa messenger web interface.

##  What I Learned & What I Would Change Today
Looking back at this code with my current knowledge of Backend Development and Software Architecture, there are several critical flaws that I would handle completely differently today:

*   **Security Vulnerability (`eval`):** The code uses `eval()` to parse numbers, which is a severe security risk (Code Injection). Today, I strictly use type casting like `int()` or `float()` and validate all external inputs.
*   **Poor DOM Traversal:** The script relies on absolute XPaths and `time.sleep()`. Modern scraping requires explicit waits (`WebDriverWait`) and robust, relative CSS selectors.
*   **Lack of OOP & Clean Architecture:** The code is procedural and tightly coupled. A modern approach would involve separating the scraping logic, data parsing, and data storage into distinct, testable classes (OOP).
*   **Maintainability:** Hardcoded paths and lack of proper error handling make this script fragile.

This project was a great stepping stone, but my current focus has shifted towards building secure, scalable backend architectures and APIs.
