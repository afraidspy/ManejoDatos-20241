public class NumeroComplejo {
	
    private float parteReal;
    private float parteImaginaria;

    public NumeroComplejo(float parteReal, float parteImaginaria) {
        this.parteReal = parteReal;
        this.parteImaginaria = parteImaginaria;
    }

    public float obtenerParteReal() {
        return parteReal;
    }

    public float obtenerParteImaginaria() {
        return parteImaginaria;
    }


    public NumeroComplejo sumar(NumeroComplejo otroComplejo) {
        double nuevaParteReal = this.parteReal + otroComplejo.obtenerParteReal();
        double nuevaParteImaginaria = this.parteImaginaria + otroComplejo.obtenerParteImaginaria();
		
        return new NumeroComplejo(nuevaParteReal, nuevaParteImaginaria);
    }

    public NumeroComplejo restar(NumeroComplejo otroComplejo) {
        double nuevaParteReal = this.parteReal - otroComplejo.obtenerParteReal();
        double nuevaParteImaginaria = this.parteImaginaria - otroComplejo.obtenerParteImaginaria();
        return new NumeroComplejo(nuevaParteReal, nuevaParteImaginaria);
    }

    @Override
    public String toString() {
        if (parteImaginaria >= 0) {
            return parteReal + " + " + parteImaginaria + "i";
        } else {
            return parteReal + " - " + Math.abs(parteImaginaria) + "i";
        }
    }

    public static void main(String[] args) {
        NumeroComplejo complejo1 = new NumeroComplejo(3, -2);
        NumeroComplejo complejo2 = new NumeroComplejo(1, 4);

        NumeroComplejo resultadoSuma = complejo1.sumar(complejo2);
        NumeroComplejo resultadoResta = complejo1.restar(complejo2);

        System.out.println("Resultado de la suma: " + resultadoSuma);
        System.out.println("Resultado de la resta: " + resultadoResta);
    }
}
