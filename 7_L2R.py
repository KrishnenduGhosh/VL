import numpy as np
import pandas as pd

from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Ridge
from sklearn import linear_model
from sklearn.linear_model import ElasticNet
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score

# Function to make predictions
def prediction(X_test, clf_object):
	# Predicton on test with giniIndex
	y_pred = clf_object.predict(X_test)
	#print("Predicted values:")
	#print(y_pred)
	return y_pred

def write_L2R():
	GS_dict = {}
	f1 = open("8_Result/trec_eval/test/GS.txt", "r")
	for x in f1:
#		print(x)
		xpart = str(x).split(" ")
		xxpart = xpart[2].split(":")
		GS_list = []
		key = xxpart[0] + ":" + xxpart[1]
		if key not in GS_dict:
			GS_list.append(xxpart[2])
			GS_dict[key] = GS_list
		else:
			GS_list = GS_dict[key]
			GS_list.append(xxpart[2])
			GS_dict[key] = GS_list
	f1.close()
	print("len(GS_dict): ",len(GS_dict))
	f2 = open("7_Reranked/rerank.txt", "r")
	for x in f2:
		xpart = str(x).split(",")
		key = xpart[0] + ":" + xpart[1]
		if key in GS_dict:
			GS_list = GS_dict[key]
			if xpart[2] in GS_list:
				f3 = open("7_Reranked/L2R.txt","a+")
				f3.write(x.replace("\n","") + ",1\n")
				f3.close()
		else:
			f3 = open("7_Reranked/L2R.txt","a+")
			f3.write(x.replace("\n","") + ",0\n")
			f3.close()
	f2.close()

# Driver code
def main():
	 
	# Building Phase
	data = pd.read_csv('7_Reranked/L2R.txt',sep= ',')
#	print("data.head(): ",data.head())

	X = data.iloc[:,3:9]
	y = data.iloc[:,9]
	print("X.shape(): ",X.shape)
	print("y.shape(): ",y.shape)

	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

	# initialization phase
	reg_LR = LinearRegression()
	reg_LOG = LogisticRegression(random_state=0, solver='lbfgs', multi_class='multinomial')
	reg_R = Ridge(alpha=1.0)
	reg_L = linear_model.Lasso(alpha=0.1)
	reg_E = ElasticNet(random_state=0)
	reg_SVR = SVR(gamma='scale', C=1.0, epsilon=0.2)

	# Training and testing phase
	print("Writing results for Linear Regression")
	model = reg_LR.fit(X_train, y_train)
	coeff_df = pd.DataFrame(reg_LR.coef_, X.columns, columns=['Coefficient'])
	print("coeff_df: ",coeff_df)
	y_pred = prediction(X_test, model)
	print("Mean squared error: %.2f"%mean_squared_error(y_test, y_pred))
#	print("Variance score: %.2f"%r2_score(y_test, y_pred))
	file = open("pred_A.data", "w")
	for line in y_pred:
		file.write(str(line) + "\n")
	file.close()

	print("Writing results for Logistic Regression")
	model = reg_LOG.fit(X_train, y_train)
	y_pred = prediction(X_test, model)
	coeff_df = pd.DataFrame(reg_LR.coef_, X.columns, columns=['Coefficient'])
	print("coeff_df: ",coeff_df)
	print("Mean squared error: %.2f"%mean_squared_error(y_test, y_pred))
#	print("Variance score: %.2f"%r2_score(y_test, y_pred))
	file = open("pred_B.data", "w")
	for line in y_pred:
		file.write(str(line) + "\n")
	file.close()

	print("Writing results for Ridge Regression")
	model = reg_L.fit(X_train, y_train)
	y_pred = prediction(X_test, model)
	coeff_df = pd.DataFrame(reg_LR.coef_, X.columns, columns=['Coefficient'])
	print("coeff_df: ",coeff_df)
	print("Mean squared error: %.2f"%mean_squared_error(y_test, y_pred))
#	print("Variance score: %.2f"%r2_score(y_test, y_pred))
	file = open("pred_C.data", "w")
	for line in y_pred:
		file.write(str(line) + "\n")
	file.close()

	print("Writing results for Lasso Regression")
	model = reg_L.fit(X_train, y_train)
	y_pred = prediction(X_test, model)
	coeff_df = pd.DataFrame(reg_LR.coef_, X.columns, columns=['Coefficient'])
	print("coeff_df: ",coeff_df)
	print("Mean squared error: %.2f"%mean_squared_error(y_test, y_pred))
#	print("Variance score: %.2f"%r2_score(y_test, y_pred))
	file = open("pred_D.data", "w")
	for line in y_pred:
		file.write(str(line) + "\n")
	file.close()

	print("Writing results for ElasticNet Regression")
	model = reg_E.fit(X_train, y_train)
	y_pred = prediction(X_test, model)
	coeff_df = pd.DataFrame(reg_LR.coef_, X.columns, columns=['Coefficient'])
	print("coeff_df: ",coeff_df)
	print("Mean squared error: %.2f"%mean_squared_error(y_test, y_pred))
#	print("Variance score: %.2f"%r2_score(y_test, y_pred))
	file = open("pred_E.data", "w")
	for line in y_pred:
		file.write(str(line) + "\n")
	file.close()

# Calling main function
if __name__=="__main__":
	write_L2R()
	main()
