class Graf:

  def __init__(self, directed=False):
    self.connection = {}
    self.directed = directed

  def add_connection(self, A, B, weight=None):
    self.connection.setdefault(A, []).append((B, weight))
    if not self.directed and A != B:
      self.connection.setdefault(B, []).append((A, weight))
    else:
      self.connection.setdefault(B, [])

  def has_loop(self):
    return any(p == t for p, ts in self.connection.items() for t, _ in ts)

  def has_weights(self):
    return any(w is not None for ts in self.connection.values() for _, w in ts)

  def is_connected(self):
    if not self.connection:
      return True
    done, stack = set(), [next(iter(self.connection))]
    while stack:
      u = stack.pop()
      if u not in done:
        done.add(u)
        stack.extend(n for n, _ in self.connection[u])
    return len(done) == len(self.connection)

  def analyze(self):
    print(
        f"Body: {len(self.connection)} | "
        f"Orientovaný: {'Ano' if self.directed else 'Ne'} | "
        f"Ohodnocený: {'Ano' if self.has_weights() else 'Ne'} | "
        f"Smyčka: {'Ano' if self.has_loop() else 'Ne'} | "
        f"Souvislý: {'Ano' if self.is_connected() else 'Ne'}"
    )
    print(f"Data: {self.connection}\n")

g = Graf(directed=False)
g.add_connection("A", "B", 5)
g.add_connection("B", "C")
g.analyze()