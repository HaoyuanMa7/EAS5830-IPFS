import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	
	# Pinata API endpoint
	url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
	
	# Headers with Pinata credentials
	headers = {
		"Content-Type": "application/json",
		"pinata_api_key": "0ac24669f793e58f09cd",
		"pinata_secret_api_key": "37a1972ccc27fd2d482d3d3d5873501d5621b3998a461f049aa371e84644f9cc"
	}
	
	# Pinata expects the JSON data directly in the payload
	payload = {
		"pinataContent": data,
		"pinataMetadata": {
			"name": "ipfs_data.json"
		}
	}
	
	# Send POST request
	response = requests.post(url, json=payload, headers=headers)
	
	# Parse response to get CID
	response_json = response.json()
	cid = response_json['IpfsHash']
	
	return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE
	# Use public IPFS gateway to retrieve the content
	url = f"https://ipfs.io/ipfs/{cid}"
	
	# Get the content from IPFS
	response = requests.get(url)
	
	# Parse the JSON content into a dictionary
	data = response.json()
	
	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data
