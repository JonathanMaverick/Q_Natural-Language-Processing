import csv

with open('Qualification/SMS_train.csv', newline='', encoding='latin-1') as csvfile:
    reader = csv.DictReader(csvfile)
    pos = 0;
    neg = 0;
    
    for row in reader:
        try:
            review = row['Message_body']
            label = row['Label']
        except ValueError:
            continue
        
        
        if label == "Non-Spam":
            with open('pos.txt', 'a', encoding='utf-8') as file:
                file.write(review + '\n')
                pos = pos + 1;
        elif label == "Spam":
            with open('neg.txt', 'a', encoding='utf-8') as file:
                file.write(review + '\n')
                    
                    
        print(pos, neg)
