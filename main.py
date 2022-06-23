from flask import Flask, render_template, request
import controller

from flask_cors import CORS
app = Flask(__name__)



@app.route('/get_result')
def my_form_post():
    result = {}
    start_date = request.args.get("sDate")
    end_date = request.args.get("eDate")
    result= controller.generator(start_date, end_date)
    
    return result
    
@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add("Access-Control-Allow-Headers", '*')
  return response

if __name__ == '__main__':
    app.run(debug=True)