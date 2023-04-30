from instance import server
from flask import render_template
from src.constants import states_constant, property_types_constant, auction_types_constant

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

    return render_template(
        'highlights.html',
        len = len(houses),
        houses = houses,
        property_types = property_types_constant.property_types,
        auction_types = auction_types_constant.auction_types,
        states = states_constant.states
    )


@app.route('/sobre', methods=['GET'])
def about():
    return render_template('about.html')