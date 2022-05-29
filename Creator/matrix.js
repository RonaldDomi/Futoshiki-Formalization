class Matrix{
	constructor(matrix,rows,cols) {
		this.matrix = matrix;
		this.rows = rows;
		this.cols = cols;
	}

	static create_void_matrix(rows,cols){
		let m = new Array(rows);
		for (let i = 0 ; i < rows ; i++){
			m[i] = new Array(cols);
		}
		return new Matrix(m,rows,cols);
	}

	static initialise_matrix(m){
		for (let i = 0; i < m.rows; i++){
			for (let j = 0; j < m.cols; j++) {
				m.matrix[i][j] = 0;
			}
		}
		return m;
	}

	static create_matrix_tab(tab,rows,cols){
		let x = 0;
		let m = this.create_void_matrix(rows,cols);
		for (let i = 0; i < rows; i++){
			for (let j = 0; j < cols; j++) {
				m.matrix[i][j] = tab[x];
				x++;
			}
		}
		return m;
	}

	static sum(m1,m2){
		if (m1.cols === m2.cols && m1.rows === m2.rows) {
			let m = this.create_void_matrix(m1.rows, m1.cols);
			for (let i = 0; i < m.rows; i++) {
				for (let j = 0; j < m.cols; j++) {
					m.matrix[i][j] = m1.matrix[i][j] - (-m2.matrix[i][j]);
				}
			}
			return m;
		}
		else alert("il faut que les matrice soit de même taille");
	}

	static multiplicate(m1,m2){
		if (m1.cols === m2.rows) {
			let m = this.create_void_matrix(m1.rows, m2.cols);
			m = this.initialise_matrix(m);
			for (let i = 0; i < m.rows; i++) {
				for (let j = 0; j < m.cols; j++) {
					for (let r = 0; r < m1.cols; r++) {
						m.matrix[i][j] = m.matrix[i][j] - (-m1.matrix[i][r] * m2.matrix[r][j]);
					}
				}
			}
			return m;
		}
		else alert("il faut que le nombre de colonne de la 1er matrice soit égale au nombre de ligne de la seconde");
	}

	static transpose(m1){
		let m = Matrix.create_void_matrix(m1.cols, m1.rows);
		for(let i = 0 ; i < m1.rows ; i++)
		{
			for(let j = 0 ; j < m1.cols ; j++)
			{
				m.matrix[j][i] = m1.matrix[i][j];
			}
		}
		return m;
	}



	static print_mat(m,p){
		p.innerHTML = "";
		for (let i = 0 ; i < m.rows ; i++){
			let l = p.appendChild(document.createElement("div"));
			l.classList.add("lign");
			let ligne = document.getElementsByClassName("lign");
			for (let j = 0 ; j < m.cols ; j++){
				let x = ligne[i].appendChild(document.createElement("div"));
				x.classList.add("pos"+i);
				x.classList.add("pos");
				let pos = document.getElementsByClassName("pos"+i);
				pos[j].innerHTML = (m.matrix[i][j]);
			}
			p.appendChild(document.createElement("br"));
		}
	}

	static init_mat_print(m,r,c,nb_mat){
		m.innerHTML = "";
		for (let i = 0 ; i < r ; i++){
			let l = m.appendChild(document.createElement("div"));
			l.classList.add("lignem"+nb_mat);
			l.classList.add("ligne");
			let ligne = document.getElementsByClassName("lignem"+nb_mat);
			for (let j = 0 ; j < c ; j++){
				let x = ligne[i].appendChild(document.createElement("input"));
				x.classList.add("mat"+nb_mat);
				x.setAttribute("type","number");
				x.setAttribute("min","0");
				x.setAttribute("max",r);
				if (j != c-1)
				{
					x = ligne[i].appendChild(document.createElement("select"));
					x.setAttribute("class", "mat1");
					let ss3 = x.appendChild(document.createElement("option"));
					ss3.setAttribute("value","|");
					ss3.innerHTML = "|";
					let ss1 = x.appendChild(document.createElement("option"));
					ss1.setAttribute("value",">");
					ss1.innerHTML = ">";
					let ss2 = x.appendChild(document.createElement("option"));
					ss2.setAttribute("value","<");
					ss2.innerHTML = "<";
				}
			}
			if(i != r-1)
			{
				l = m.appendChild(document.createElement("div"));
				l.classList.add("signem"+nb_mat);
				l.classList.add("signe");
				let signe = document.getElementsByClassName("signem"+nb_mat);
				for (let j = 0 ; j < c ; j++){
					let x;
					x = signe[i].appendChild(document.createElement("select"));
					x.setAttribute("class", "mat1");
					let ss3 = x.appendChild(document.createElement("option"));
					ss3.setAttribute("value","-");
					ss3.innerHTML = "-";
					let ss1 = x.appendChild(document.createElement("option"));
					ss1.setAttribute("value","^");
					ss1.innerHTML = "^";
					let ss2 = x.appendChild(document.createElement("option"));
					ss2.setAttribute("value","v");
					ss2.innerHTML = "v";	
				}
			}
		}
	}
}

function create_tab(x){
	let tab = [];
	for (let i = 0 ; i < x.length  ; i++){
		console.log("tab de " + i + " " + x[i].value);
	  	tab.push(x[i].value);
	}
	return tab;
}

function getM1() {
	let dim = document.getElementById('dim').value;
	if(dim > 0){
		const m1 = create_tab(document.getElementsByClassName('mat1'));
		console.log("m1 : " + 1);
		return Matrix.create_matrix_tab(m1,dim * 2 - 1,dim * 2 - 1);
	}
	const m1 = create_tab(document.getElementsByClassName('mat1'));
	return Matrix.create_matrix_tab(m1,3,3);

}

function getM2() {
	let r2 = document.getElementById('lm2').value;
	let c2 = document.getElementById('cm2').value;
	if(r2 > 0 && c2 > 0){
		const m2 = create_tab(document.getElementsByClassName('mat2'));
		return Matrix.create_matrix_tab(m2,r2,c2);
	}
	const m2 = create_tab(document.getElementsByClassName('mat2'));
	return Matrix.create_matrix_tab(m2,3,3);
}

function somme(){
	let m1 = getM1();
	let m2 = getM2();
	let m = Matrix.sum(m1,m2);
	const p = document.getElementById('para');
	Matrix.print_mat(m,p);
}

function produit(){
	let m1 = getM1();
	let m2 = getM2();
	let m = Matrix.multiplicate(m1,m2);
	const p = document.getElementById('para');
	Matrix.print_mat(m,p);
}

function transposer(){
	let m1 = getM1();
	let m = Matrix.transpose(m1);
	const p = document.getElementById('para');
	Matrix.print_mat(m,p);
}

function affichage(){
	let dim = document.getElementById('dim').value;
	let m = document.getElementsByClassName('m');
	if (dim > 0){
		Matrix.init_mat_print(m[0],dim,dim,1);
	}
	else ;
}

function download(filename, text) {
  var element = document.createElement('a');
  element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
  element.setAttribute('download', filename);

  element.style.display = 'none';
  document.body.appendChild(element);

  element.click();

  document.body.removeChild(element);
}

function def(signe){
	if(signe == "&lt;"){
		return "<";
	}
	else return signe;
}

function envoyer(){
	let dim = document.getElementById('dim').value;
	if(dim == ""){
		dim = 3;
	}
	let titre = document.getElementById('titre').value;
	const m = create_tab(document.getElementsByClassName('mat1'));
	chaine = "";
	chaine = chaine.concat(dim + "\n");
	let i = 0;
	while(i < m.length){
		chaine = chaine.concat("\n");
		for(let j = 0; j < dim * 2 - 1; j++){
			if(j == 0 || j%2 == 0){
				console.log("mot" + m[i]);
				if(m[i] == ""){
					chaine = chaine.concat("0 ");
				}
				else chaine = chaine.concat(def(m[i]) + " ");
			}
			else{
				if(m[i] == ""){
					chaine = chaine.concat("| ");
				}
				else chaine = chaine.concat(def(m[i]) + " ");
			} 
			i++;
		}
		if(i != m.length)
		{
			chaine = chaine.concat("\n");
			for(let j = 0; j < dim ; j++){
				if(m[i] == ""){
					chaine = chaine.concat("-   ");
				}
				else chaine = chaine.concat(m[i] + "   "); 
				i++;
			}
		}
	}
	download(titre,chaine);
}