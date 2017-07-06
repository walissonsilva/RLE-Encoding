#include <bits/stdc++.h>

using namespace std;

int main(){
	ifstream arquivo("IMG.txt");
	stringstream ss;

	if (!arquivo.is_open()){
		return 1;
	}

	string line, RLE(""), aux;
	char pixel;
	vector<string> img;
	int qtd = 0;

	while(getline(arquivo, line)){
		img.push_back(line);

		int i = 0;
		while(i < line.size()){
			qtd = 0;
			pixel = line[i];
			while(pixel == line[i] && i < line.size()){
				i++;
				qtd++;
			}

			ss.clear();
			if (pixel == '0')
				ss << qtd << 'Z';
			else
				ss << qtd << 'U';
			ss >> aux;

			RLE += aux;
		}

		RLE += "00";
	}

	RLE += "01";

	cout << "\n########### IMAGEM ORIGINAL #############\n";
	cout << "Tamanho da imagem original: " << (img.size() * img[0].size()) * sizeof(char) << endl;
	cout << "Tamanho após a codificação: " << (RLE.size() * sizeof(char)) << endl;
	cout << RLE << endl;

	// ####################### DECODIFICAÇÃO ############################

	return 0;
}