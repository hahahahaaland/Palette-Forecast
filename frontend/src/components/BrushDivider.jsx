// A loose brush-stroke underline, used consistently beneath page headers
// to mark "this is where a section begins" — a painterly stand-in for
// the usual plain <hr>.
function BrushDivider({ className = "w-40" }) {
    return (
        <svg
            viewBox="0 0 220 16"
            className={className}
            preserveAspectRatio="none"
            aria-hidden="true"
        >
            <path
                d="M4 10c30-6 60-8 90-6s70 6 122 2"
                stroke="#fb7185"
                strokeWidth="6"
                strokeLinecap="round"
                fill="none"
                opacity="0.9"
            />
            <path
                d="M4 12c40-4 90-5 130-3s60 3 86 1"
                stroke="#172554"
                strokeWidth="2.5"
                strokeLinecap="round"
                fill="none"
                opacity="0.7"
            />
        </svg>
    );
}

export default BrushDivider;
