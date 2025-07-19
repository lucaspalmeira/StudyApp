from flask import Blueprint, jsonify, request
from pymongo import MongoClient

items_bp = Blueprint('items', __name__, url_prefix='/api/items')

client = MongoClient("mongodb://172.17.0.2:27017/")
db = client["gh32"]
protein_entries = db['protein_entries']
seqs_entries = db['seqs_entries']
desc_entries = db['desc_entries']
taxon_entries = db['taxon_entries']

# busca todos os documentos dentro de protein_entries que tenham 
# o número de ec da requisição
def find_ec(ec):
    list_entries = []
    ec_number = list(protein_entries.find({'ec_number': ec}, {'_id':0}))
    for i in ec_number:
        # percorre todos os dicionários
        if i['ec_number'] == ec:
            list_entries.append(i['entry'])
    return list_entries

# busca todos os documentos dentro de uma coleção a partir de uma lista de entradas
# e retorna uma lista de dicionários contendo os dados de cada entrada
def find_docs_byec(list_entries, collection):
    list_seqs = []
    for entry in list_entries:
        list_dict_seqs = list(collection.find({'entry': entry}, {'_id':0}))
        for i in list_dict_seqs:
            list_seqs.append(i)
    return list_seqs

@items_bp.route('/metadata', methods=['GET'])
def get_metadata():
    items = list(protein_entries.find({}, {'_id': 0}))
    if items:
        return jsonify(items)
    else:
        return jsonify({"message": "No metadata found"}), 404

@items_bp.route('/descriptors', methods=['GET'])
def get_descriptors():
    descriptors = list(desc_entries.find({}, {'_id': 0}))
    if descriptors:
        return jsonify(descriptors)
    else:
        return jsonify({"message": "No descriptors found"}), 404

@items_bp.route('/sequences', methods=['GET'])
def get_sequences():
    sequences = list(seqs_entries.find({}, {'_id': 0}))
    if sequences:
        return jsonify(sequences)
    else:
        return jsonify({"message": "No sequences found"}), 404

@items_bp.route('/taxon', methods=['GET'])
def get_taxon():
    taxon = list(taxon_entries.find({}, {'_id': 0}))
    if taxon:
        return jsonify(taxon)
    else:
        return jsonify({"message": "No taxonomic data found"}), 404

@items_bp.route('/ec/<ec_number>', methods=['GET'])
def get_metadata_by_id(ec_number):
    ec_data = list(protein_entries.find({'ec_number': ec_number}, {'_id':0}))

    if ec_data:
        return jsonify(ec_data)
    else:
        return jsonify({"message": f"No proteins found for EC number {ec_number}"}), 404

@items_bp.route('/sequences/<ec_number>', methods=['GET'])
def get_fasta_by_id(ec_number):
       
    list_entries = find_ec(ec_number)

    if list_entries:
        return jsonify(find_docs_byec(list_entries, seqs_entries))
    
    else:
        return jsonify({"message": f"No sequences found for EC number {ec_number}"}), 404

@items_bp.route('/descriptors/<ec_number>', methods=['GET'])
def get_descriptors_by_id(ec_number):
    list_entries = find_ec(ec_number)

    if list_entries:
        return jsonify(find_docs_byec(list_entries, desc_entries))
    
    else:
        return jsonify({"message": f"No descriptions found for EC number {ec_number}"}), 404

@items_bp.route('/taxon/<ec_number>', methods=['GET'])
def get_taxon_by_id(ec_number):
    list_entries = find_ec(ec_number)

    if list_entries:
        return jsonify(find_docs_byec(list_entries, taxon_entries))
    
    else:
        return jsonify({"message": f"No taxonomic data found for EC number {ec_number}"}), 404