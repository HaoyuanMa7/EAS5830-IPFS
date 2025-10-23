import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	# Convert dictionary to JSON bytes
	json_data = json.dumps(data).encode('utf-8')
	
	# Use a public IPFS API endpoint (ipfs.tech previously ipfs.io)
	url = "https://ipfs.tech/api/v0/add"
	
	# Prepare the file to upload
	files = {
		'file': ('data.json', json_data, 'application/json')
	}
	
	# Send POST request to add the file
	response = requests.post(url, files=files)
	
	# Parse the response to get the CID (Hash)
	response_json = response.json()
	cid = response_json['Hash']
	
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
