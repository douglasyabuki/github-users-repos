# 📦 GitHub Users Repositories

A simple app to fetch and store public GitHub repositories for a given user.

---

## ✅ Project Checklist

### 🛠 Requirements

- [ ] GitHub Integration  
  - [ ] Use `GET https://api.github.com/users/{username}/repos`
  - [ ] Use only these fields from each repo:
    - [ ] `name`
    - [ ] `html_url`
    - [ ] `description`
    - [ ] `language`
  - [ ] Handle GitHub's unauthenticated rate limit (60 requests/hour)

---

### 🖼 Frontend

- [ ] Input form to submit a GitHub username
- [ ] Display the response from the web server
- [ ] Keep UI clean or styled (be ready to explain design choices)

---

### 🌐 Web Server

- [ ] Receive requests from the frontend
- [ ] Fetch repos from GitHub API
- [ ] Extract required fields from **first 5 repositories**
- [ ] Store data (file, no-SQL, or your choice)
- [ ] If user exists:
  - [ ] Update the record  
- [ ] If user does not exist:
  - [ ] Create a new record
- [ ] Respond with:
  - [ ] Repo data (4 fields per repo)
  - [ ] Whether the user is new or existing

---

### 🔁 Data Refresh

- [ ] Background task to refresh data regularly for all stored users
