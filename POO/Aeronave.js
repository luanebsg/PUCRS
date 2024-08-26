class Aeronave {
    constructor(prefixo, tipo, velocidadeCruzeiro, autonomia) {
        this.prefixo = prefixo;
        this.tipo = tipo;
        this.velocidadeCruzeiro = velocidadeCruzeiro;
        this.autonomia = autonomia;
    }

    // Métodos comuns para todas as aeronaves
    getPrefixo() {
        return this.prefixo;
    }

    getTipo() {
        return this.tipo;
    }

    getVelocidadeCruzeiro() {
        return this.velocidadeCruzeiro;
    }

    getAutonomia() {
        return this.autonomia;
    }
}

// Aeronave particular
class AeronavePequenoPorte extends Aeronave {
    constructor(prefixo, velocidadeCruzeiro, autonomia, empresaManutencao) {
        super(prefixo, 'Pequeno Porte', velocidadeCruzeiro, autonomia);
        this.empresaManutencao = empresaManutencao;
    }

    getEmpresaManutencao() {
        return this.empresaManutencao;
    }
}

// Aeronave comercial de passageiros
class AeronaveComercialPassageiros extends Aeronave {
    constructor(prefixo, velocidadeCruzeiro, autonomia, capacidadePassageiros, companhiaAerea) {
        super(prefixo, 'Comercial Passageiros', velocidadeCruzeiro, autonomia);
        this.capacidadePassageiros = capacidadePassageiros;
        this.companhiaAerea = companhiaAerea;
    }

    getCapacidadePassageiros() {
        return this.capacidadePassageiros;
    }

    getCompanhiaAerea() {
        return this.companhiaAerea;
    }
}

// Aeronave comercial de carga
class AeronaveComercialCarga extends Aeronave {
    constructor(prefixo, velocidadeCruzeiro, autonomia, capacidadeCarga, companhiaAerea) {
        super(prefixo, 'Comercial Carga', velocidadeCruzeiro, autonomia);
        this.capacidadeCarga = capacidadeCarga;
        this.companhiaAerea = companhiaAerea;
    }

    getCapacidadeCarga() {
        return this.capacidadeCarga;
    }

    getCompanhiaAerea() {
        return this.companhiaAerea;
    }
}
