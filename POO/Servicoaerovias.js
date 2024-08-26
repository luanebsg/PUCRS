class ServicoAerovias {
    constructor() {
        this.aerovias = [];
    }

    adicionarAerovia(aerovia) {
        this.aerovias.push(aerovia);
    }

    listarAerovias() {
        return this.aerovias;
    }

    getAeroviaPorIdentificador(identificador) {
        return this.aerovias.find(aerovia => aerovia.getIdentificador() === identificador);
    }
}
