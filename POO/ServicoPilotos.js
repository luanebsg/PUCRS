class ServicoPilotos {
    constructor() {
        this.pilotos = [];
    }

    adicionarPiloto(piloto) {
        this.pilotos.push(piloto);
    }

    getPilotoPorMatricula(matricula) {
        return this.pilotos.find(piloto => piloto.getMatricula() === matricula);
    }

    listarPilotos() {
        return this.pilotos;
    }
}
