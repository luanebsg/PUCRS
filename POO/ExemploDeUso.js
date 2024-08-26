// Criação dos serviços
const servicoPilotos = new ServicoPilotos();
const servicoAeronaves = new ServicoAeronaves();
const servicoAerovias = new ServicoAerovias();

// Adicionando pilotos
const piloto1 = new Piloto('12345', 'João Silva', true);
servicoPilotos.adicionarPiloto(piloto1);

// Adicionando aeronaves
const aeronave1 = new AeronavePequenoPorte('PP-ABC', 500, 1500, 'Empresa A');
servicoAeronaves.adicionarAeronave(aeronave1);

// Adicionando aerovias
const aerovia1 = new Aerovia('BR001', 'Aeroporto A', 'Aeroporto B', 1000);
servicoAerovias.adicionarAerovia(aerovia1);

// Listando pilotos
console.log(servicoPilotos.listarPilotos());

// Listando aeronaves
console.log(servicoAeronaves.listarAeronaves());

// Listando aerovias
console.log(servicoAerovias.listarAerovias());
