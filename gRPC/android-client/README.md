## gRPC Client Android

# To test

To test, you just need to install the *app-debug.apk*

## Building using [Android Studio](https://developer.android.com/studio/)...
1. Open Android Studio and launch the Android SDK manager from it (Tools | Android | SDK Manager)
1. Ensure the following components are installed and updated to the latest version.
 1. *Android SDK Platform-Tools* 1. *Android Support Repository*
 1. *Google Repository*
 1. Return to Android Studio and select *Open an existing Android Studio project*
 1. Select the **studion-app-android** directory.

### Compile and run After synchronizing and indexing dependencies, simply compile and run the project from the **app** directory.

**Building** To build the samples after you have applied the changes above, you can use the build/run option in Android Studio, or build directly from the command line if you prefer.

**IMPORTANT** Ensure you have set the ANDROID_HOME environment variable. cd /path/to/android-basic-samples export ANDROID_HOME = /path/to/android/sdk ./gradlew build
