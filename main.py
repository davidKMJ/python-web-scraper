from flask import Flask, render_template, request, redirect, send_file
from extractors.berlinstartupjobs import extract_berlinstartupjobs_jobs
from extractors.weworkremotely import extract_weworkremotely_jobs
from extractors.web3 import extract_web3_jobs
from extractors.remoteok import extract_remoteok_jobs
from file import save_to_file

app = Flask("JobScrapper")

db = {}

@app.route("/")
def home():
    return render_template("home.html", name="David")

@app.route("/search")
def hello():
    keyword = request.args.get("keyword")
    if keyword is None:
        return redirect("/")
    if keyword in db:
        jobs = db[keyword]
    else:
        jobs = []
        jobs += extract_berlinstartupjobs_jobs(keyword)
        jobs += extract_weworkremotely_jobs(keyword)
        jobs += extract_web3_jobs(keyword)
        jobs += extract_remoteok_jobs(keyword)
        db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs=jobs)


@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword is None:
        return redirect("/")
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")
    save_to_file(keyword, db[keyword])
    return send_file(f"{keyword}.csv", as_attachment=True)

app.run("0.0.0.0", port=5500, debug=True)