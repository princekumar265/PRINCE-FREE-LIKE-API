export default function handler(req, res) {
  res.status(200).json({
    success: true,
    message: "PRINCE FREE LIKE API is ONLINE",
    owner: "PrinceGamer07",
    status: "Running"
  });
}
