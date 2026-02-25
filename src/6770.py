import requests
from bs4 import BeautifulSoup

def get_stock_price(stock_id):
    url = f"https://tw.stock.yahoo.com/quote/{stock_id}"
    
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")


    # 取得目前股價（class 可能會變動）
    price = soup.find("span", {"class": "Fz(32px)"})
    print(f"{stock_id} 今日股價3: {price.text}")
    if price:
        print(f"{stock_id} 今日股價: {price.text}")
        
    else:
        print("找不到股價資訊（可能網站結構改變）")

if __name__ == "__main__":
    get_stock_price("6770")