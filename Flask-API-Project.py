#Creating a simple portfolio page using flask
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Resume</title>

    <!-- INTERNAL CSS -->
    <style>
        body {
            font-family: Arial, Helvetica, sans-serif;
            background: #f4f6f9;
            margin: 0;
            padding: 0;
        }

        .container {
            width: 70%;
            margin: 30px auto;
            background: #ffffff;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 18px rgba(0,0,0,0.1);
        }

        header {
            text-align: center;
            margin-bottom: 25px;
        }

        header h1 {
            font-size: 36px;
            color: #2a4d69;
            margin-bottom: 5px;
        }

        .tagline {
            color: #4f6d7a;
            font-size: 16px;
            margin-bottom: 10px;
        }

        .contact p {
            margin: 3px 0;
        }

        h2 {
            color: #2a4d69;
            border-left: 6px solid #2a4d69;
            padding-left: 8px;
            margin-bottom: 10px;
        }

        .section {
            margin-bottom: 25px;
        }

        .item h3 {
            margin: 5px 0;
            color: #1e3d59;
        }

        .skills {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 8px;
        }

        .skills li {
            background: #e6f0fa;
            padding: 8px;
            border-radius: 5px;
        }

        ul {
            margin: 0;
            padding-left: 20px;
        }
    </style>
</head>

<body>

    <div class="container">

        <!-- HEADER -->
        <header>
            <h1>Naman Kumar</h1>
            <p class="tagline">Engineering Student | Problem Solver | Tech Enthusiast</p>

            <div class="contact">
                <p>Email: namankraj2@Gmail.com</p>
                <p>Phone: +91 74888xxxxxx</p>
                <p>Location: Jaipur, India</p>
            </div>
        </header>

        <!-- PROFILE -->
        <section class="section">
            <h2>Profile</h2>
            <p>
                I am an engineering student passionate about technology, innovation, and problem-solving,
                with strong interest in real-world projects and technical learning.
            </p>
        </section>

        <!-- EDUCATION -->
        <section class="section">
            <h2>Education</h2>

            <div class="item">
                <h3>Bachelor of Engineering (Your Branch)</h3>
                <p>Your College Name | 2023 – Present</p>
                <p>CGPA: 8.0 (or your score)</p>
            </div>

            <div class="item">
                <h3>Higher Secondary Education</h3>
                <p>Your School Name | 2021 – 2023</p>
                <p>Percentage: 85% (or your score)</p>
            </div>
        </section>

        <!-- SKILLS -->
        <section class="section">
            <h2>Skills</h2>
            <ul class="skills">
                <li>Programming: C, C++, Python, Java (Basics)</li>
                <li>Web: HTML, CSS, JavaScript</li>
                <li>Tools: AutoCAD, MATLAB</li>
                <li>Problem Solving</li>
                <li>Teamwork & Communication</li>
                <li>Project Management</li>
            </ul>
        </section>

        <!-- PROJECTS -->
        <section class="section">
            <h2>Projects</h2>

            <div class="item">
                <h3>Mini Project Title</h3>
                <p>Short description of your project, including tools used and your contribution.</p>
            </div>

            <div class="item">
                <h3>Another Project Title</h3>
                <p>Short description of what you built and the skills you learned.</p>
            </div>

        </section>

        <!-- CERTIFICATIONS -->
        <section class="section">
            <h2>Certificates</h2>
            <ul>
                <li>Certification Name – Platform</li>
                <li>Certification Name – Platform</li>
                <li>Certification Name – Platform</li>
            </ul>
        </section>

        <!-- SOCIAL LINKS -->
        <section class="section">
            <h2>Contact / Social Links</h2>
            <ul>
                <li>LinkedIn: your-link</li>
                <li>GitHub: your-profile</li>
                <li>Portfolio Website (optional)</li>
            </ul>
        </section>

    </div>

</body>
</html>
"""

if __name__=='__main__':
    app.run()
