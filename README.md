Markdown
# TfL BikePoint Data Fetcher

A straightforward Python script that extract real-time docking station data from the Transport for London (TfL) BikePoint API. It automatically timestamps, handles errors including a retry mechanism and logs execution at various stages.

---

## 🚀 Features

* **Real-time Data Retrieval:** Extracts live bikepoint data from the official TfL API.
* **Resilient Retry Logic:** Automatically retries up to 5 times with a 10-second delay if it encounters server errors (5xx) or network issues.
* **Automated Data Organization:** Saves the JSON payloads into a data directory, with timestamped filenames.
* **Robust Logging:** Keeps track of successes, retries, and failures in a logging directory.

---
