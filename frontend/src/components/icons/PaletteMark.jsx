// A small hand-drawn artist's palette with a brush resting across it.
// Colors are locked to the app's existing navy + baby-pink palette so it
// never clashes no matter where it's placed.
function PaletteMark({ className = "w-8 h-8" }) {
    return (
        <svg
            viewBox="0 0 64 64"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
            className={className}
            role="img"
            aria-label="Artist's palette"
        >
            {/* palette board */}
            <path
                d="M32 6C17 6 6 16.5 6 29c0 8 5.5 11 11 11 2.5 0 4-1.3 4-3.3
                   0-1.7-1.3-2.4-1.3-4.2 0-2.6 2.4-4.5 5.6-4.5 9 0 16.7-7 16.7-14.3
                   C42 8.6 37.6 6 32 6Z"
                fill="#ffe4e6"
                stroke="#172554"
                strokeWidth="2"
                strokeLinejoin="round"
            />
            {/* thumb hole */}
            <ellipse cx="18" cy="35" rx="3.4" ry="4.4" fill="#fff" stroke="#172554" strokeWidth="1.6" />
            {/* paint dabs */}
            <circle cx="17" cy="16" r="3" fill="#fb7185" />
            <circle cx="27" cy="11" r="3" fill="#172554" />
            <circle cx="36" cy="14" r="3" fill="#fda4af" />
            <circle cx="30" cy="22" r="3" fill="#1d4ed8" />
            {/* brush handle */}
            <line x1="40" y1="46" x2="55" y2="18" stroke="#172554" strokeWidth="3" strokeLinecap="round" />
            {/* brush ferrule + bristle tip */}
            <path
                d="M55 18l3-6c1-2 3.2-1 2.4 1l-3 6-2.4-1Z"
                fill="#fb7185"
                stroke="#172554"
                strokeWidth="1.4"
                strokeLinejoin="round"
            />
        </svg>
    );
}

export default PaletteMark;
