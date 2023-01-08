from instance import server
from flask import render_template
from src.controllers.liveness_controller import LivenessController

app = server.app

@app.route('/destaques', methods=['GET'])
def highlights():
    houses = [
        {
            'image': 'images/casa_1.jpg',
            'auction_type': 'Leilão Judicial',
            'property_name': 'Apartamento Vila Anglo Brasileira 108,59 m²',
            'property_address': 'Rua volta Redonda',
            'offer_1': '1ª praça: R$ 1.201.496,13',
            'offer_2': '2ª praça: R$ 1.201.496,13',
            'evaluation': 'Avaliação: R$ 1.201.496,13'
        },
        {
            'image': 'images/casa_2.jpg',
            'auction_type': 'Leilão Judicial',
            'property_name': 'Apartamento Vila Anglo Brasileira 108,59 m²',
            'property_address': 'Rua volta Redonda',
            'offer_1': '1ª praça: R$ 1.201.496,13',
            'offer_2': '2ª praça: R$ 1.201.496,13',
            'evaluation': 'Avaliação: R$ 1.201.496,13'
        },
        {
            'image': 'images/casa_3.jpg',
            'auction_type': 'Leilão Judicial',
            'property_name': 'Apartamento Vila Anglo Brasileira 108,59 m²',
            'property_address': 'Rua volta Redonda',
            'offer_1': '1ª praça: R$ 1.201.496,13',
            'offer_2': '2ª praça: R$ 1.201.496,13',
            'evaluation': 'Avaliação: R$ 1.201.496,13'
        },
        {
            'image': 'images/casa_4.jpg',
            'auction_type': 'Leilão Judicial',
            'property_name': 'Apartamento Vila Anglo Brasileira 108,59 m²',
            'property_address': 'Rua volta Redonda',
            'offer_1': '1ª praça: R$ 1.201.496,13',
            'offer_2': '2ª praça: R$ 1.201.496,13',
            'evaluation': 'Avaliação: R$ 1.201.496,13'
        },
        {
            'image': 'images/casa_5.jpg',
            'auction_type': 'Leilão Judicial',
            'property_name': 'Apartamento Vila Anglo Brasileira 108,59 m²',
            'property_address': 'Rua volta Redonda',
            'offer_1': '1ª praça: R$ 1.201.496,13',
            'offer_2': '2ª praça: R$ 1.201.496,13',
            'evaluation': 'Avaliação: R$ 1.201.496,13'
        },
    ]
    return render_template('highlights.html', len = len(houses), houses = houses)

@app.route('/card_description/<int:image_code>', methods=['GET'])
def lionel(image_code):
    return render_template('card_description.html', image_code="{}.jpg".format(image_code))