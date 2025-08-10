import math

def caclular_mosaic(W, H, A, B, M, C):
    # calcular cuantas baldosas se necesitan horizontal y vetical
    horizontalBaldosas = math.ceil(W / A)  
    verticalBaldosas = math.ceil(H / B)    
    
    # calcular baldosas necesarias
    totalBaldosas = horizontalBaldosas * verticalBaldosas
    
    # cantidad de baldosas
    baldosasNecesarias = math.ceil(totalBaldosas / 10)

    # costo por pila de baldosas
    costoBaldosas = baldosasNecesarias * M
    
    # calcular la longitud total de cortes necesarios
    totalCortesNecesarios = 0
    
    # Cortes horizontales (si W no es divisible por A necesitamos cortar los azulejos del borde derecho)
    if W % A != 0:
        # Solo cortamos la parte que sobra del ancho
        cortesHorizontal = verticalBaldosas * (W % A)
        totalCortesNecesarios += cortesHorizontal
    
    # Cortes verticales (si H no es divisible por B necesitamos cortar los azulejos del borde inferior)  
    if H % B != 0:
        # Solo cortamos la parte que sobra del alto
        cortesVertical = horizontalBaldosas * (H % B)
        totalCortesNecesarios += cortesVertical
    
    # Caso especial: si hay sobrantes en ambas direcciones, la esquina necesita cortes adicionales
    if W % A != 0 and H % B != 0:
        # La esquina inferior derecha necesita cortes adicionales
        totalCortesNecesarios += 4
    
    # costo de cortes
    costoCortes = totalCortesNecesarios * C
    
    # costo total
    costoTotal = costoBaldosas + costoCortes
    
    print(f"Dimensiones de la pared: {W}×{H}")
    print(f"Dimensiones del azulejo: {A}×{B}")
    print(f"Baldosas necesarias: {horizontalBaldosas}×{verticalBaldosas} = {totalBaldosas}")
    print(f"Pilas de baldosas a comprar: {baldosasNecesarias}")
    print(f"Costo de baldosas: {baldosasNecesarias} pilas × ${M} = ${costoBaldosas}")
    print(f"Longitud total de cortes: {totalCortesNecesarios} pulgadas")
    print(f"Costo de cortes: {totalCortesNecesarios} × ${C} = ${costoCortes}")
    print(f"Costo total: ${costoBaldosas} + ${costoCortes} = ${costoTotal}")
    
    return costoTotal

def main():
    print("Ingrese los valores W, H, A, B, M, C separados por espacios:")
    try:
        W, H, A, B, M, C = map(int, input().split())
        
        # control de altura y ancho de la pared para cumplir con los requisitos
        if not (1 <= W <= 10**9 and 1 <= H <= 10**9):
            print("Error: W y H deben estar entre 1 y 10^9")
            return
        if not (1 <= A <= W and 1 <= B <= H):
            print("Error: A debe estar entre 1 y W, B debe estar entre 1 y H")
            return
        if not (1 <= M <= 10**9 and 1 <= C <= 10**9):
            print("Error: M y C deben estar entre 1 y 10^9")
            return
        
        # Resolver el problema
        result = caclular_mosaic(W, H, A, B, M, C)
        print(f"\nRespuesta: {result}")
        
    except ValueError:
        print("Error: Por favor ingrese 6 números enteros válidos")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()
