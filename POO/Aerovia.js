class Aerovia {
    constructor(identificador, origem, destino, tamanho) {
        this.identificador = identificador;
        this.origem = origem;
        this.destino = destino;
        this.tamanho = tamanho;
    }

    getIdentificador() {
        return this.identificador;
    }

    getOrigem() {
        return this.origem;
    }

    getDestino() {
        return this.destino;
    }

    getTamanho() {
        return this.tamanho;
    }
}
