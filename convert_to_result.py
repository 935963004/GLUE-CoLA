import pickle

f = open('./data/models/electra_large/test_predictions/cola_test_1_predictions.pkl', 'rb')
data = pickle.loads(f.read())

print("Writing results to CoLA.tsv...")
with open("CoLA.tsv", "w") as f1:
    f1.write("index	prediction")
    f1.write('\n')
    for key, value in data.items():
        f1.write(str(key))
        f1.write('\t')
        f1.write('0' if value[0] > value[1] else '1')
        f1.write('\n')
print("Done!")

f.close()
