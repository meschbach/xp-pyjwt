# Example of using Python's PyJWT

## Example Encoding

`python encode.py some-secret audience 1`

Will produce:

```plain
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJhdWRpZW5jZSIsInN1YiI6IjEifQ.17brM7M4qT_FU93vEzcUyTS72iQhiwPf_HV8KETKun0
```

## Example Decoding

`python decode.py some-secret audience eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJhdWRpZW5jZSIsInN1YiI6IjEifQ.17brM7M4qT_FU93vEzcUyTS72iQhiwPf_HV8KETKun0`

Will produce:

```plain
1
```
