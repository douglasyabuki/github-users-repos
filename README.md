# 📦 GitHub Users Repositories

A simple app to fetch and store public GitHub repositories for a given user.

---
# 🐳 How to Run This App with Docker
## 1. Build the Docker Image
From the root of the project (where Dockerfile is located), run:

```
docker build -t github-user-repos .
```

This builds the image and names it github-user-repos.

## 2. Run the Container
Run the container and expose port 8000 to your local machine:
```
docker run -p 8000:8000 github-user-repos
```
Or run in detached mode:
```
docker run -d -p 8000:8000 github-user-repos
```

Now the app is accessible at:
```
http://localhost:8000
```

## 3. Test the API
Check health:
```
curl http://localhost:8000/api/health
```

Test in browser:
```
http://localhost:8000/
```

## ✅ Project Checklist

### 🛠 Requirements

- [x] GitHub Integration  
  - [x] Use `GET https://api.github.com/users/{username}/repos`
  - [x] Use only these fields from each repo:
    - [x] `name`
    - [x] `html_url`
    - [x] `description`
    - [x] `language`
  - [x] Handle GitHub's unauthenticated rate limit (60 requests/hour)

---

### 🖼 Frontend

- [x] Input form to submit a GitHub username
- [x] Display the response from the web server
- [x] Keep UI clean or styled (be ready to explain design choices)

---

### 🌐 Web Server

- [x] Receive requests from the frontend
- [x] Fetch repos from GitHub API
- [x] Extract required fields from **first 5 repositories**
- [x] Store data (file, no-SQL, or your choice)
- [x] If user exists:
  - [x] Update the record  
- [x] If user does not exist:
  - [x] Create a new record
- [x] Respond with:
  - [x] Repo data (4 fields per repo)
  - [x] Whether the user is new or existing

---

### 🔁 Data Refresh

- [x] Background task to refresh data regularly for all stored users
