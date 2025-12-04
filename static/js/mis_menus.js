/* ====== FUNCIONALIDAD: MIS MENÚS ====== */
document.addEventListener('DOMContentLoaded', () => {
    // Animación suave al cargar tarjetas de menús
    const tarjetasMenus = document.querySelectorAll('#tarjeta_menu');
    tarjetasMenus.forEach((tarjeta, index) => {
        tarjeta.style.opacity = '0';
        tarjeta.style.transform = 'translateY(20px)';
        
        setTimeout(() => {
            tarjeta.style.transition = 'all 0.5s cubic-bezier(0.4, 0, 0.2, 1)';
            tarjeta.style.opacity = '1';
            tarjeta.style.transform = 'translateY(0)';
        }, index * 100);
    });
});
