# 📦 GitHub Users Repositories

A simple app to fetch and store public GitHub repositories for a given user.

---

## ✅ Project Checklist

### 🛠 Requirements

- [x] GitHub Integration  
  - [x] Use `GET https://api.github.com/users/{username}/repos`
  - [x] Use only these fields from each repo:
    - [x] `name`
    - [x] `html_url`
    - [x] `description`
    - [x] `language`
  - [ ] Handle GitHub's unauthenticated rate limit (60 requests/hour)

---

### 🖼 Frontend

- [x] Input form to submit a GitHub username
- [x] Display the response from the web server
- [ ] Keep UI clean or styled (be ready to explain design choices)

---

### 🌐 Web Server

- [x] Receive requests from the frontend
- [x] Fetch repos from GitHub API
- [x] Extract required fields from **first 5 repositories**
- [ ] Store data (file, no-SQL, or your choice)
- [ ] If user exists:
  - [ ] Update the record  
- [ ] If user does not exist:
  - [ ] Create a new record
- [ ] Respond with:
  - [x] Repo data (4 fields per repo)
  - [ ] Whether the user is new or existing

---

### 🔁 Data Refresh

- [ ] Background task to refresh data regularly for all stored users
