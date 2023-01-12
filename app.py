from flask import Flask, render_template, request, redirect
from db_utils import new_item_db

app = Flask(__name__)

# Main page
@app.route('/')
def index():
    return render_template('index.html')


# Add a new item onto the database
@app.route('/new_item', methods=["GET", "POST"])
def new_item():
    if request.method == "POST":
        name=request.form.get("name")
        new_item_db(name)
        return redirect("/")

        

    else:
        return render_template('new_item.html')



    

@app.route('/history')
def item():
    return render_template('history.html')




if __name__ == '__main__':
    app.run()