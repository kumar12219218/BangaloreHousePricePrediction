from flask import *
app=Flask(__name__)
#app=Flask(__name__,template_folder="templates",static_folder="static")


@app.route('/')
def index():
    return render_template(
        'index1.html',data=["red","yellow","green"])
        
#data=[{'name':'red'}, {'name':'green'}, {'name':'blue'}])
@app.route("/test" , methods=['GET', 'POST'])
def test():
    select = request.form.get('comp_select')
    return(str(select)) # just to see what select is


# @app.route("/")
# def home():
#     return render_template("index1.html")


@app.route("/login",methods=["GET","POST"])
def login():
    uname=request.args.get("Name")
    passw=request.args.get("password")
    select=request.form.get("selected")
    return (str(select))

@app.route("/about")
def about_page():
    return "<h1>This is about page</h1>"

if __name__=="__main__":
    app.run(debug=True)