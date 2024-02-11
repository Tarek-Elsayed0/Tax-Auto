import csv

for year in range(2019, 2024):
    with open(f"Sales_{year}.csv", "a", encoding="utf-8-sig", newline="") as csv_file:
        writer = csv.writer(csv_file)
       
        for month in range(12):
            i=0
            while True:
                try:
                    i+=1
                    with open(f"{year}_{month}_{i}.csv", "r", encoding="utf-8-sig") as file:
                        next(file)
                        reader = csv.reader(file)
                        for line in reader:
                            writer.writerow(line)
                            # print(line)
                        # writer.writerows(reader)
                    
                #     for line in file.readlines()[1:]:
                #         print(line)
                    
                except:
                    print(f"{year}_{month} Done!")
                    break
