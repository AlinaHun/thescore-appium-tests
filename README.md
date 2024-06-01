# thescore-appium-tests

# Automated Testing for Mobile App

This project is for automated testing of a mobile application using Appium and Python.
The tests navigate through the app and verify various functionalities.

## Prerequisites

- [Java 11](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html)
- [Node.js](https://nodejs.org/) and [npm](https://www.npmjs.com/get-npm)
- [Appium 2.x](http://appium.io/docs/en/about-appium/intro/)
- [Android SDK](https://developer.android.com/studio#downloads)
- [Python 3.x](https://www.python.org/downloads/)
- [Gradle](https://gradle.org/install/)

## Setup Instructions

1. **Install Java:**

   Download and install Java 11 from
   the [official website](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html).

2. Install Node.js and npm:

   Download and install Node.js from the [official website](https://nodejs.org/). npm is included with Node.js.

3. Install Appium:

   Install Appium globally using npm:

    ```sh
    npm install -g appium
    
4. Create and Activate a Virtual Environment:

   Navigate to your project directory and create a virtual environment:

       python -m venv venv

   Activate the virtual environment:

    - Windows:

               .\venv\Scripts\activate

    - macOS/Linux:

               source venv/bin/activate

5. Install Python packages:

   With the virtual environment activated, install the required Python packages:

       pip install -r requirements.txt

6. Configure Appium:

   Start Appium server from the command line:

       appium

7. Install the UI Automator 2 driver by running the following command in your terminal:

          appium driver install uiautomator2

8. Start Android Emulator:

   Make sure you have an Android emulator running. You can start it from Android Studio or the command line:

       emulator -avd <your_emulator_name>

9. Running Tests:

   To run the tests, you can use the following Gradle tasks:

       gradle runTests

## Project Structure

- build.gradle: Gradle configuration file.
- requirements.txt: Python dependencies.
- src/test/python: Directory containing Python test scripts and page object models.

## Sample Tests

Here are the steps automated in the tests:

1. Open a league page of your choice.
2. Verify that the expected page opens correctly.
3. Tap on a sub-tab standings.
4. Verify that you are on the correct tab and that the data is displayed correctly and corresponds to the league,
   team, or player from step 1.
5. Verify that back navigation returns you to the previous page correctly.

## Configurable Data

You can configure league, team, and player names in the data.yaml file,
making it easy to update the tests without changing the test scripts directly.

## Example data.yaml:

leagues:
"name": "NBA"

team:
"name": "BMA"

## Updating Tests

To update the league, team, or player names, simply modify the data.yaml file. The test scripts will use these values
dynamically.

## Deactivating the Virtual Environment

When you are done working, you can deactivate the virtual environment by running:

      deactivate

###

     