from flask import Flask, render_template, request 

app = Flask(__name__) 

@app.route("/", methods=["GET", "POST"]) 
def index(): 
    er = None 
    if request.method == "POST": 
        try: 
            likes = int(request.form["likes"]) 
            comments = int(request.form["comments"]) 
            shares = int(request.form["shares"]) 
            followers = int(request.form["followers"]) 
            
            if followers == 0: 
                return "Jumlah followers tidak boleh 0!" 
            
            #Hitung Engagement Rate 
            er = ((likes + comments + shares) / followers) * 100 
            
        except ValueError: 
            return "Input tidak valid! Masukkan angka yang benar." 
        
    return render_template("badan.html", er=round(er, 2) if er is not None else None) 

if __name__ == "__main__": 
    app.run (debug=True)
