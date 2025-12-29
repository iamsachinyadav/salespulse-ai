function SentimentChart({ sentiment }) {
  const positive = sentiment?.positive ?? 0;
  const negative = sentiment?.negative ?? 0;
  const neutral = sentiment?.neutral ?? 0;

  return (
    <div>
      <p>Positive: {positive}</p>
      <p>Negative: {negative}</p>
      <p>Neutral: {neutral}</p>
    </div>
  );
}

export default SentimentChart;
