#include <string>
#include <list>

namespace zsbh
{
namespace json
{

enum TokenType {
    TOKEN_NULL = 1 << 1,    //null
    TOKEN_OBJ_L = 1 << 2,   //{
    TOKEN_OBJ_R = 1 << 3,   //}
    TOKEN_ARR_L = 1 << 4,   //[
    TOKEN_ARR_R = 1 << 5,   //]
    TOKEN_QUOTE = 1 << 6,   //"
    TOKEN_SEPARATE = 1 << 7,//:
    TOKEN_NUMBER = 1 << 8,  //^[-1-9][0-9]*$
    TOKEN_KEY = 1 << 9,     //^"[a-zA-Z_][a-zA-Z0-9_]*"$
    TOKEN_STRING = 1 << 10, //^".*"$
    TOKEN_BOOL = 1 << 11,   //true | false
};

struct Token {
    TokenType type;
    std::string value;
    /*source info*/
};

class Tokenizer
{
private:
    std::string text;
    std::list<Token> tokens;

/* data */
public:
    Tokenizer(const std::string &t):text(t) {}
    ~Tokenizer();

    void tokenize();
};

Tokenizer::~Tokenizer()
{
}

void Tokenizer::tokenize() {

}

} // namespace json  
} // namespace zsbh




