class ServicoAeronaves {
    constructor() {
        this.aeronaves = [];
    }

    adicionarAeronave(aeronave) {
        this.aeronaves.push(aeronave);
    }

    getAeronavePorPrefixo(prefixo) {
        return this.aeronaves.find(aeronave => aeronave.getPrefixo() === prefixo);
    }

    listarAeronaves() {
        return this.aeronaves;
    }
}
