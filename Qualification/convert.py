import csv

with open('Qualification/reviews_data.csv', newline='', encoding='latin-1') as csvfile:
    reader = csv.DictReader(csvfile)
    pos = 0;
    neg = 0;
    
    for row in reader:
        try:
            review = row['Review']
            rating = float(row['Rating'].split()[0])
        except ValueError:
            continue
        
        if rating > 2:
            with open('pos.txt', 'a', encoding='utf-8') as file:
                file.write(review + '\n')
                pos = pos + 1;
        else:
            with open('neg.txt', 'a', encoding='utf-8') as file:
                file.write(review + '\n')
                neg = neg + 1;
                    
                    
        print(pos, neg)
