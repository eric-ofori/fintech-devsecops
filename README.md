# 🗓️ Week 1: DevSecOps & Tooling Foundations

---

## ✅ Goals

- Understand DevOps, CI/CD, and DevSecOps concepts  
- Learn Git and GitHub fundamentals  
- Install and configure key tools: Docker, Git, Terraform, AWS CLI  
- Build and dockerize an intermediate Python Flask microservice  
- Push the project to GitHub  

---

## 📚 Learning Resources

| Topic               | Resource                                                                                         |
| ------------------- | ------------------------------------------------------------------------------------------------ |
| DevOps Basics       | [DevOps Foundations – LinkedIn Learning](https://www.linkedin.com/learning/devops-foundations)   |
| Git & GitHub        | [GitHub Git Handbook](https://guides.github.com/introduction/git-handbook/)                      |
| Docker Fundamentals | [Docker Getting Started](https://docs.docker.com/get-started/)                                   |
| Terraform Basics    | [Terraform by HashiCorp](https://developer.hashicorp.com/terraform/tutorials)                    |
| AWS CLI             | [Install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) |

---

## 🛠️ **Tools to Install**

| Tool      | Purpose                      | Install Guide                                                                                                                              |
| --------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Git       | Version control              | [https://git-scm.com/downloads](https://git-scm.com/downloads)                                                                             |
| Docker    | Containerization             | [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)                                           |
| AWS CLI   | AWS cloud interaction        | [https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) |
| Terraform | Infrastructure as Code (IaC) | [https://developer.hashicorp.com/terraform/downloads](https://developer.hashicorp.com/terraform/downloads)                                 |
| VS Code   | Code editor (optional)       | [https://code.visualstudio.com/](https://code.visualstudio.com/)                                                                           |

---

## 🧱 **Step-by-Step Breakdown**

---

### 🔹 Step 1: Understand the Core Concepts

| Concept       | Summary                                                               |
| ------------- | --------------------------------------------------------------------- |
| **DevOps**    | Combines development & operations for faster, reliable delivery.      |
| **CI/CD**     | Automates build, test, and deployment.                                |
| **DevSecOps** | Integrates security into every phase of DevOps (shift-left security). |

📺 **Watch:**

* [What is DevSecOps? (YouTube)](https://www.youtube.com/watch?v=cHEk2VbBvC4)

✍️ **Write a note or blog post summarizing what you’ve learned.**

---

### 🔹 Step 2: Install Tools

Open a terminal (PowerShell, Terminal, Bash), and install the tools:

#### ✅ Git

```bash
git --version
```

#### ✅ Docker

```bash
docker --version
```

#### ✅ AWS CLI

```bash
aws --version
aws configure
```

#### ✅ Terraform

```bash
terraform version
```

---

### 🔹 Step 3: Set Up the Project Folder

```bash
mkdir fintech-devsecops
cd fintech-devsecops
mkdir app .github terraform manifests
```

---

### 🔹 Step 4: Create the Flask Microservice

📄 **app/app.py**

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    1: {"name": "Alice", "balance": 5000},
    2: {"name": "Bob", "balance": 3000},
}

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

@app.route('/users/<int:user_id>/deposit', methods=['POST'])
def deposit(user_id):
    amount = request.json.get("amount")
    if not amount or amount <= 0:
        return jsonify({"error": "Invalid amount"}), 400
    users[user_id]["balance"] += amount
    return jsonify(users[user_id])

@app.route('/users/<int:user_id>/withdraw', methods=['POST'])
def withdraw(user_id):
    amount = request.json.get("amount")
    if not amount or amount <= 0 or amount > users[user_id]["balance"]:
        return jsonify({"error": "Invalid withdrawal"}), 400
    users[user_id]["balance"] -= amount
    return jsonify(users[user_id])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

📄 **app/requirements.txt**

```
flask
```

---

### 🔹 Step 5: Dockerize the Flask App

📄 **Dockerfile** (placed at the root of the project)

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY app/ /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "app.py"]
```

---

### 🔹 Step 6: Build and Run the App in Docker

```bash
# Build the Docker image
docker build -t fintech-user-service .

# Run the container
docker run -p 5000:5000 fintech-user-service
```

🔗 Test it in your browser: [http://localhost:5000/users](http://localhost:5000/users)

🧪 Or test with curl:

```bash
curl http://localhost:5000/users
curl -X POST -H "Content-Type: application/json" -d '{"amount": 500}' http://localhost:5000/users/1/deposit
```

---

### 🔹 Step 7: Push Code to GitHub

```bash
git init
git add .
git commit -m "Week 1: Add intermediate Flask app"
git remote add origin https://github.com/YOUR_USERNAME/fintech-devsecops.git
git push -u origin main
```

---
