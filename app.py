from flask import Flask,render_template,request,jsonify
# from flask_assets import Environment, Bundle
import pickle
import pandas as pd
travel_df = pickle.load(open('travel.pkl','rb'))

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/explore')
def explore():
    return render_template('explore.html',
                           places=travel_df.to_dict(orient='records'))


@app.route('/card/<int:card_id>')
def card_detail(card_id):
    card = travel_df.loc[travel_df['sr'] == card_id].to_dict(orient='records')
    if card:
        return render_template('card_detail.html', card=card[0])
    else:
        return "Card not found", 404

if __name__ == '__main__':
    app.run(debug=True)