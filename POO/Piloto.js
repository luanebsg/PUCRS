class Piloto {
    constructor(matricula, nome, habilitacaoAtiva) {
        this.matricula = matricula;
        this.nome = nome;
        this.habilitacaoAtiva = habilitacaoAtiva;
    }
    
    // Métodos de acesso e modificação (getters e setters)
    getMatricula() {
        return this.matricula;
    }

    getNome() {
        return this.nome;
    }

    isHabilitacaoAtiva() {
        return this.habilitacaoAtiva;
    }

    setHabilitacaoAtiva(status) {
        this.habilitacaoAtiva = status;
    }
}
