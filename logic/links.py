from engine import app as web, cast, request

@web.route("/")
def homepage():
    return cast("index.html")

@web.route("/about")
def about():
    return cast("about.html")

@web.route("/qualifications")
def qualifications():
    return cast("qualifications.html")

@web.route("/projects")
def projects():
    return cast("projects.html")

@web.route("/resume")
def resume():
    return cast("resume.html")

@web.route("/contact")
def contact():
    return cast("contact.html")

@web.route("/faqs")
def faqs():
    return cast("faqs.html")

@web.route("/feedback")
def feedback():
    return cast("feedback.html")