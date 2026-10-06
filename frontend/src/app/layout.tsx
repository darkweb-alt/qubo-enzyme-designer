import "./globals.css";

export const metadata = {
  title: "Quantum Bio-Forge",
  description: "Quantum-directed enzyme active-site optimization engine",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}