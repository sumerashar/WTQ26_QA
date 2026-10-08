import requests
def test_api_status():
    url = "https://jsonplaceholder.typicode.com/posts/1" #I NEED TO CHANge it on day
    r = requests.get(url, timeout = 10)
    print(f"Status :{r.status_code}")
    assert r.status_code == 200, "API FAILED"
    print("Pass - API working")
    #API VALIDATION LOGIC

    data = r.json()
    assert "userId" in data, "Missing field - AI flagged as Invalid"
    print("Pass- AI Validation: Schema correct")


if __name__ =="__main__":
    test_api_status()    

