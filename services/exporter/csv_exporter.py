import csv

def export_csv(path, data):
    with open(path,"w",newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["class","count"])
        for k,v in data.items():
            writer.writerow([k,v])
